import json
from django.http import HttpResponse
from django.views import View
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import BlogPost, BlogRubric, LikeDislike
from .forms import PostForm, CommentForm


class IndexPage(ListView):

    paginate_by = 5
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class DetailPost(FormView, DetailView):

    model = BlogPost
    form_class = CommentForm
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(DetailPost, self).get_context_data(**kwargs)
        context['comment_form'] = self.get_form()
        context['slug'] = BlogPost.objects.all()
        context['comments'] = self.object.comment.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post_id = self.object.pk
        comment.save()
        return super().form_valid(comment)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={
            'rubric_slug': self.object.rubric_name.slug,
            'slug': self.object.slug,
        })


class TagPosts(ListView):

    paginate_by = 5
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self, **kwargs):
        tags = list()
        tags.append(self.kwargs['tag_slug'])
        return BlogPost.objects.filter(tags__name__in=tags)


class RubricPage(ListView):

    paginate_by = 5
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self, **kwargs):
        slug = BlogRubric.objects.get(slug=self.kwargs['rubric_slug'])
        return BlogPost.objects.filter(rubric_name=slug.id)


class RubricIndexPage(ListView):

    template_name = 'blog/rubrics.html'
    context_object_name = 'post'
    queryset = BlogPost.objects.filter()


class VoteView(View):
    model = None
    vote_type = None

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        try:
            like_dislike = LikeDislike.objects.get(
                content_type=ContentType.objects.get_for_model(obj),
                object_id=obj.id, user=request.user)
            if like_dislike.vote is not self.vote_type:
                like_dislike = self.vote_type
                like_dislike.save(update_fields=['vote'])
                result = True
            else:
                like_dislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True

        return HttpResponse(
            json.dumps({
                "result": result,
                "like_count": obj.votes.likes().count(),
                "dislike_count": obj.votes.dislikes().count(),
                "sum_rating": obj.votes.sum_rating()
            }),
            content_type="application/json"
        )


def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            post = BlogPost.objects.get(title=new_post)
            tags = request.POST['tags'].split()
            for tag in tags:
                new_post.tags.add(tag)
            return redirect('blog:detail', post.rubric_name.slug, post.slug)
        return render(request, 'blog/form_post.html', {'form': form})
    return render(request, 'blog/form_post.html', {'form': form})


def edit_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:detail', post.rubric_name.slug, post.slug)
        return render(request, 'blog/form_post.html', {'form': form})
    form = PostForm(instance=post)
    return render(request, 'blog/form_post.html', {'form': form})

from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, View
from .models import BlogPost, BlogRubric
from .forms import PostForm
from django.utils.text import slugify


class IndexPage(ListView):

    paginate_by = 3
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class DetailPost(DetailView):

    model = BlogPost
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = BlogPost.objects.all()
        return context


class TagPosts(ListView):

    paginate_by = 3
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self, **kwargs):
        tags = list()
        tags.append(self.kwargs['tag_slug'])
        return BlogPost.objects.filter(tags__name__in=tags)


class RubricPage(ListView):

    paginate_by = 3
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self, **kwargs):
        slug = BlogRubric.objects.get(slug=self.kwargs['rubric_slug'])
        return BlogPost.objects.filter(rubric_name=slug.id)

    def get_context_data(self, **kwargs):
        slug = BlogRubric.objects.get(slug=self.kwargs['rubric_slug'])
        context = super().get_context_data(**kwargs)
        context['rubrics'] = BlogRubric.objects.all()
        context['current_rubrics'] = BlogRubric.objects.get(pk=slug.id)
        return context


class RubricIndexPage(ListView):

    paginate_by = 3
    template_name = 'blog/rubrics.html'
    context_object_name = 'posts'
    queryset = BlogRubric.objects.filter()


def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            post = BlogPost.objects.get(title=new_post)
            post.tags.add(request.POST['tags'])
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

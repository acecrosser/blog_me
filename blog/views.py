from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, View
from .models import BlogPost, BlogRubric
from .forms import PostForm
from django.utils.text import slugify


class IndexPage(ListView):

    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = BlogPost.objects.filter()


class DetailPost(DetailView):

    model = BlogPost
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = BlogPost.objects.all()
        return context


class TagPosts(ListView):

    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self, **kwargs):
        tags = list()
        tags.append(self.kwargs['tag_slug'])
        return BlogPost.objects.filter(tags__name__in=tags)


class RubricPage(ListView):

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
            # slug = slugify(post.title)
            # print(slug)
            # post.slug = slug
            return redirect('blog:index_page')
        return render(request, 'blog/add_post.html', {'form': form})
    return render(request, 'blog/add_post.html', {'form': form})


def edit_post(request, pk):
    pass

from django.shortcuts import (
            render, get_object_or_404,
            )
from django.views import generic

from .models import (
            Post, Author, Tag
            )


class IndexView(generic.ListView):
    # model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.order_by('-created')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None, id=1):
        return get_object_or_404(Post, pk=id)

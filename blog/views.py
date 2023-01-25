from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

from django.views import generic
from .models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = 'blog/home.html'


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

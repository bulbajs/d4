from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = '-time_in_Post'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    paginate_by = 2


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context



class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'

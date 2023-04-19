from django.http import Http404
from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Post
from blog.serializers import PostSerializer


class IndexPage(TemplateView):
    template_name = 'home_page.html'


class PostsListView(ListView):
    template_name = 'posts.html'
    queryset = Post.objects.all()


class PostsDetailView(DetailView):
    template_name = 'post.html'

    def get_object(self, queryset=None):
        postId = self.kwargs.get('pk')
        try:
            post = Post.objects.get(pk=postId)
        except:
            raise Http404('post Not Found')
        return post


class PostListApiView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailApiView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

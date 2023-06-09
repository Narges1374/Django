from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import IndexPage, PostsDetailView, PostsListView, PostViewset

urlpatterns = [
    path('', IndexPage.as_view(), name='home-page'),
    path('posts', PostsListView.as_view(), name='posts-list'),
    path('post/<slug:slug>', PostsDetailView.as_view(), name='post-detail'),

]

router = DefaultRouter()
router.register(r'post-api', PostViewset)

urlpatterns += router.urls

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import IndexPage, PostsDetailView, PostsListView, PostViewset

urlpatterns = [
    path('', IndexPage.as_view()),
    path('posts', PostsListView.as_view()),
    path('posts/<pk>', PostsDetailView.as_view()),

]

router = DefaultRouter()
router.register(r'post-api', PostViewset)

urlpatterns += router.urls

from django.urls import path, include
from .views import (
  PostCreateView,
  PostListView,
)
app_name = 'gram'
urlpatterns = [
  path('',PostListView.as_view(),name='allPosts'),
    path('new/',PostCreateView.as_view(),name='createPost'),
]
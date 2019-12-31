from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import (
  PostCreateView,
  PostListView,
)
app_name = 'gram'
urlpatterns = [
  path('',PostListView.as_view(),name='allPosts'),
    path('new/',PostCreateView.as_view(),name='createPost'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
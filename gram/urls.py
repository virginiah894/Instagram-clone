from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .import views
from .views import (
  PostCreateView,
  PostListView,
  PostDetailView,

)
app_name = 'gram'
urlpatterns = [
    path('',PostListView.as_view(),name='allPosts'),
    path('new/',PostCreateView.as_view(),name='createPost'),
    path('<int:id>',PostDetailView.as_view(), name= 'postDetails'),
    path('search/',views.search_posts ,name='search_posts'),
    path('profile/', views.profile , name = 'profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
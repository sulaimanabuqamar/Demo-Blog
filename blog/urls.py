from django.urls import path
from .views import blog_list, blog_detail, blog_delete, blog_create, blog_edit

urlpatterns = [
    path('posts/', blog_list, name="blog_list"),
    path('posts/<int:post_id>/', blog_detail, name='blog_detail'),
    path('posts/create/', blog_create, name="blog_create"),
    path('posts/<int:post_id>/delete/', blog_delete, name='blog_delete'),
    path('blog/posts/<int:post_id>/edit/', blog_edit, name='blog_edit'),
]

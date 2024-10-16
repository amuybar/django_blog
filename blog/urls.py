from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_view, name='blog_list'),  # List all blogs
    # path('<int:id>/', views.blog_detail_view, name='blog_detail'),  # View a specific blog post
    path('<int:blog_id>/edit/', views.update_blog, name='edit_blog'),  # Edit a blog post
    path('<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),  # Delete a blog post
]

from django.urls import path, include, re_path
from rest_framework import routers
from . import views

urlpatterns = [
    path(r'posts/', views.posts_view),
    path(r'posts/<int:pk>/', views.posts_detail_view),

    path(r'feeds/', views.feeds_view),
    path(r'feeds/<username>/', views.feeds_username_view),
    path(r'feeds/following/posts/', views.feeds_following_view),
]
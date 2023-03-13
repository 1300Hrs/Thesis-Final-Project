from django.urls import path
from .views import PostListview, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path("", PostListview.as_view(), name="blog_home"),
    path("about/", views.about, name="blog_about"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("like_post/<int:pk>", views.like_view, name="like_post"),
]

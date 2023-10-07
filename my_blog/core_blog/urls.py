from django.urls import path
from .views import index, test_view, about_view, post_detail_view
from .views import (PostsListView,
                    PostDetailView,
                    PostCreateView,
                    PostDeleteView,
                    PostUpdateView,
                    UserPostListView)

urlpatterns = [
    # path('', index, name='index'),
    path('', PostsListView.as_view(), name='index'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>', post_detail_view, name='post-detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('test', test_view, name='test_view'),
    path('about', about_view, name='about_view'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.registration, name='register'),
    path('profile/', views.profile, name='profile'),
    
    # Blog Post URLs
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', views.add_comment, name='add_comment'),  # Add a new comment
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),  # Update an existing comment
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),  # Delete a comment
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
    path('tags/<slug:tag_slug>/', views.posts_by_tag, name='posts_by_tag'),

]


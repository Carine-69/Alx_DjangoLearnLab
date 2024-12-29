from django.urls import path
from django.contrib.auth import views as auth_views
form . import views

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('register/', views.registration, name='register'),
	path('profile/', views.profile, name='profile'),
	path('', views.PostListView.as_view(), name='post_list'),
    	path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    	path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    	path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    	path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
	path('', PostListView.as_view(), name='post_list'),
    	path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    	path('posts/new/', PostCreateView.as_view(), name='post_create'),
    	path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    	path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
    	# Comment URLs
    	path('posts/<int:post_id>/comment/', add_comment, name='add_comment'),
    	path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    	path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]

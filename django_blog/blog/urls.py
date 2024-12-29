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
]

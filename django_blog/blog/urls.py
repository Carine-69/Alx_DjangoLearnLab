from django.urls import path
from django.contrib.auth import views as auth_views
form . import views

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('registration/', views.registration, name='registration'),
	pth('profile', views.profile, name='profile'),
]

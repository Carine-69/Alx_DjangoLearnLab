from django.contrib import admin
from django.urls import path
from bookshelf import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line to include the admin URL
    path('', views.home, name='home'),  # Your homepage view
]

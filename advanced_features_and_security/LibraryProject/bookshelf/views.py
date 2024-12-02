# bookshelf/views.py
from django.shortcuts import render
from .models import Book

def home(request):
    # Fetch all books from the database
    books = Book.objects.all()
    # Pass the list of books to the template
    return render(request, 'home.html', {'books': books})

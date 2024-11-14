from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # Define what fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters to make it easier to sort through books
    list_filter = ('author', 'publication_year')

    # Enable search functionality for title and author
    search_fields = ('title', 'author')

# Register the Book model with the custom admin interface
admin.site.register(Book, BookAdmin)

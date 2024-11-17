# Create Operation

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output:
# <Book: 1984 by George Orwell>


# Retrieve Operation

```python
retrieved_book = Book.objects.get(title="1984")
retrieved_book
# Output:
# <Book: 1984 by George Orwell>


# Update Operation

```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
retrieved_book
# Output:
# <Book: Nineteen Eighty-Four by George Orwell>


# Delete Operation

```python
retrieved_book.delete()
Book.objects.all()
# Output:
# <QuerySet []>

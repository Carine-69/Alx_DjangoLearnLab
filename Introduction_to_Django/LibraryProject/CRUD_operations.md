# CRUD_operations.md

### Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # Expected output: <Book: 1984 by George Orwell (1949)>
retrieved_book = Book.objects.get(id=book.id)
retrieved_book.title, retrieved_book.author, retrieved_book.publication_year
# Expected output: ('1984', 'George Orwell', 1949)
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
retrieved_book.title  # Expected output: 'Nineteen Eighty-Four'
retrieved_book.delete()
Book.objects.all()  # Expected output: <QuerySet []>

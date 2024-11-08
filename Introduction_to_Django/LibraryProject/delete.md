# Delete the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

#trying to retrieve all books to confirm deletion
books = Book.objects.all()
#the book "Nineteen Eighty-Four shoild be no longer existing"
#the books list should be empty
print(books)

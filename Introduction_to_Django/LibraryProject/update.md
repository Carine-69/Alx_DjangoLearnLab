# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title and save
book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output:
# Book title should now be updated to "Nineteen Eighty-Four"
print(book.title)

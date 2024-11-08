# Retrieve the book instance by title
book = Book.objects.get(title="1984")

# Display all attributes of the retrieved book
print(book)

# Expected Output:
# The book instance should display all its fields, e.g.:
# <Book: 1984 by George Orwell, published on 1949-01-01>

book = Book.objects.get(title="1984")
book.title
# '1984'
book.author
# 'George Orwell'
book.publication_year
# 1949
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# 'Nineteen Eighty-Four'
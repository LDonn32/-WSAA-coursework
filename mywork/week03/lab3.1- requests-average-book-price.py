# a program to work out average book price from andrewbeatty1.pythonanywhere.com/books
# Author: Laura Donnelly




from bookapidao import getAllBooks

books = getAllBooks()
if not books:
    print("No books found.")
else:
    valid_books = [book for book in books if book.get("price") is not None]
    if not valid_books:
        print("No books with a valid price found.")
    else:
        total = sum(book["price"] for book in valid_books)
        count = len(valid_books)
        average = total / count
        print(f"Average of {count} books is {average:.2f}")


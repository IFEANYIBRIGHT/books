books = [
    "Book Title: The Hobbit\nPages: 47",
    "Book Title: To Kill a Mockingbird by Harper Lee (Social Justice)\nPages: 100",
    "Book Title: Rich Dad Poor Dad\nPages: 140",
    "Book Title: Surrounded by Idiots\nPages: 100"
]

while True:
    application_sample = """
***WELCOME TO THE BOOK SUGGESTION SYSTEM***
1. Get Suggestions
2. Add Book
3. Remove Book
4. Update Book
5. Show All Books
"""
    print(application_sample)

    choose = int(input("What would you like to do today: "))

    if choose == 1:
        print("\nBook Suggestions:")
        for book in books:
            print(" ", book)
        print("You can make the library grow by adding more books!\n")

    elif choose == 2:
        add_books = input("Input names of books you would like to add: ")
        books.append(add_books)
        print("Book added successfully!\n")

    elif choose == 3:
        remove_book = input("Enter book title to remove: ")
        if remove_book in books:
            books.remove(remove_book)
            print("Book removed successfully\n")
        else:
            print("Book not found\n")

    elif choose == 4:
        old_title = input("Enter old title: ")
        if old_title in books:
            index = books.index(old_title)
            new_title = input("Enter the new title: ")
            books[index] = new_title
            print("Book updated successfully\n")
        else:
            print("Book not found\n")

    elif choose == 5:
        print("\nAll Books in the Library:")
        for book in books:
            print(" ", book)
        print()
    
    else:
        print("Invalid option, please choose 1-5\n")


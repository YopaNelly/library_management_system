# Create a list of books

# stage 1

books = []

# some books
dict_1 = {
    'title': 'To Kill a Mockingbird', 
    'author': 'Harper Lee',
      'genre': 'Classic', 
      'isbn': '9780062981581'
      }
dict_2 = {
    'title': '1984', 
    'author': 'George Orwell', 
    'genre': 'Dystopian Fiction',
      'isbn': '9780451524935'
}
dict_3 = {
    'title': 'The Hitchhiker\'s Guide to the Galaxy', 
    'author': 'Douglas Adams', 
    'genre': 'Science Fiction', 
    'isbn': '9780330508117'
}


#Functio to add book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    genre = input("Enter the book genre: ")
    isbn = input("Enter the book ISBN: ")

    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "inbn": isbn
    }
    
    books.append(book)

    return books


# Function to update book
def update_book():
    title = input("Enter the book title to update: ")
    for book in books:
        if book['title'] == title:
            author = input("Enter new author name (or leave blank to skip): ")
            if author != '':
                book['author'] = author
            genre = input("Enter new book genre (or leave blank to skip): ")
            if genre != '':
                book['genre'] = genre
            isbn = input("Enter new book ISBN (or leave blank to skip): ")
            if isbn != '':
                book['isbn'] = isbn
            print("Book details updated successfully")
            return
    print("Book not found")
    return


#Function to delete an exsisting book
def delete_book():
    title = input("Enter the book title to delete: ")
    for book in books:
        if book['title'] == title:
            books.remove(book)
            print("Book deleted successfully")
            return
    print("Book not found")
    return

# Function to display all books in a formatted manner
def show_all_books():
    print("-" * 70)
    print('{:<30s} {:<25s} {:<20s} {:<15s}'.format("Title", "Author", "Genre", "ISBN"))
    print("-" * 70)
    for book in books:
        print('{:<30s} {:<25s} {:<20s} {:<15s}'.format(book['title'], book['author'], book['genre'], book['isbn']))
    print("-" * 70)

# Function to display books filtered by a specific criteria (e.g., genre)
def show_filtered_books():
    filter_by = input("Enter the filter criteria (e.g., genre): ")
    filter_value = input("Enter the {} value to filter by: ".format(filter_by))
    print("-" * 70)
    print('{:<30s} {:<25s} {:<20s} {:<15s}'.format("Title", "Author", "Genre", "ISBN"))
    print("-" * 70)
    for book in books:
        if book[filter_by] == filter_value:
            print('{:<30s} {:<25s} {:<20s} {:<15s}'.format(book['title'], book['author'], book['genre'], book['isbn']))
    print("-" * 70)

def search_book():
    search = input("Enter a search keyword eg (title, author, genre, ISBN, etc.): ")
    keyword = input("Enter the {} of the book you want to seach : ".format(search))
    matching_books = []
    for book in books:
        if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower() or keyword.lower() in book['genre'].lower() or keyword.lower() in book['isbn'].lower():
            matching_books.append(book)
    if len(matching_books) > 0:
        print("Found matching books:")
        print("-" * 70)
        print('{:<30s} {:<25s} {:<20s} {:<15s}'.format("Title", "Author", "Genre", "ISBN"))
        print("-" * 90)
        for book in matching_books:
            print('{:<30s} {:<25s} {:<20s} {:<15s}'.format(book['title'], book['author'], book['genre'], book['isbn']))
        print("-" * 90)
    else:
        print("No books found for the entered keyword")

# stage 3

# Adding sample books to the list for testing
books.append(dict_1)
books.append(dict_2)
books.append(dict_3)

# Providing options for the user to interact with the books list
while True:
    print("\nOptions:")
    print("1. Add a new book")
    print("2. Update an existing book")
    print("3. Delete an existing book")
    print("4. View all books")
    print("5. Filter books by criteria")
    print("6. search book")
    print("7. Exsit")
    choice = input("\nEnter your choice (1-7): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        show_all_books()
    elif choice == '5':
        show_filtered_books()
    elif choice == '6':
        search_book()
    elif choice == '7':    
        break
    else:
        print("Invalid choice. Try again.")

print("Thank you for using the book management system!")

#stage 4

# File Handling

import json

def save_book(books, filename):
    # converting dictionaly to JSON file strings
    json_data = json.dumps(books)

    # write the json sting to a file
    with open(filename, "w") as file:
        file.write(json_data)


save_book(books, "books.json")


def load_books(filename):
    # reade json file
    with open(filename, "r") as file:
        json_data = file.read()
    # convert JSON string to list of dictionary
    data = json.loads(json_data)
    return data


# load book and populate the table

data = load_books("books.json")
print(data)

# stage 5
# Additional function


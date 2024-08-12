import pymongo

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['library']
books_collection = db['books']

def create_book(title, author, year):
    book = {'title': title, 'author': author, 'year': year}
    books_collection.insert_one(book)
    print(f"Book '{title}' by {author} created successfully!")

def read_books():
    books = books_collection.find()
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

def update_book(title, author, year):
    books_collection.update_one({'title': title}, {'$set': {'author': author, 'year': year}})
    print(f"Book '{title}' updated successfully!")

def delete_book(title):
    books_collection.delete_one({'title': title})
    print(f"Book '{title}' deleted successfully!")

def main():
    while True:
        print("Library Management System")
        print("1. Create Book")
        print("2. Read Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter book year: "))
            create_book(title, author, year)
        elif choice == '2':
            read_books()
        elif choice == '3':
            title = input("Enter book title to update: ")
            author = input("Enter new author: ")
            year = int(input("Enter new year: "))
            update_book(title, author, year)
        elif choice == '4':
            title = input("Enter book title to delete: ")
            delete_book(title)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

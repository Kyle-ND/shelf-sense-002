DATABASE_FILE = "./database/books.txt"

DATABASE_FILE= "test_books.txt"

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    with open(DATABASE_FILE, 'a') as db:
        #db.write("Title,Author")
        pass  # Ensure the file exists

def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    
    # TODO: Append the book's title and author to the database file
    global DATABASE_FILE
    with open(DATABASE_FILE,"a") as db:
        db.write(f"\n{title},{author}")
        
        
        
def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    global DATABASE_FILE

    with open(DATABASE_FILE,"r") as db:
        content = db.readlines()
        
        for line in content:
            t,n = line.split(",")
            if title == t:
                return {"title":f"{title}","author":f"{n[:-1]}"}
            
    return None
    # TODO: Implement logic to search for a book in the database file

def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    # TODO: Read all books from the database file and return them as a list of dictionaries
    global DATABASE_FILE
    books =[]
    with open(DATABASE_FILE,"r") as db:
        lines = db.readlines()
        for line in lines:
            t,n = line.split(",")
            if t!="Title" and n!="Auther":
                books.append({"title":f"{t}","author":f"{n[:-1]}"})
            
    return books
        
        

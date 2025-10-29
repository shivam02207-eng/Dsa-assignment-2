
class BookNode:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.next = None

class BookList:
    def __init__(self):
        self.head = None

    def insertBook(self, book_id, title, author):
        new_book = BookNode(book_id, title, author)
        if not self.head:
            self.head = new_book
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_book
        print(f"Book '{title}' added successfully.\n")

    def deleteBook(self, book_id):
        current = self.head
        prev = None
        while current:
            if current.book_id == book_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"Book ID {book_id} deleted successfully.\n")
                return
            prev = current
            current = current.next
        print("Book not found.\n")

    def searchBook(self, book_id):
        current = self.head
        while current:
            if current.book_id == book_id:
                print(f"Book Found → ID: {current.book_id}, Title: {current.title}, "
                      f"Author: {current.author}, Status: {current.status}\n")
                return current
            current = current.next
        print("Book not found.\n")
        return None

    def displayBooks(self):
        if not self.head:
            print("No books available in the library.\n")
            return
        print("\nCurrent Books in Library:")
        print("-" * 50)
        current = self.head
        while current:
            print(f"ID: {current.book_id}, Title: {current.title}, "
                  f"Author: {current.author}, Status: {current.status}")
            current = current.next
        print("-" * 50 + "\n")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0

    def display(self):
        if self.isEmpty():
            print("No transactions yet.\n")
        else:
            print("\nRecent Transactions (Top → Bottom):")
            print("-" * 50)
            for transaction in reversed(self.items):
                print(transaction)
            print("-" * 50 + "\n")
            
class LibrarySystem:
    def __init__(self):
        self.book_list = BookList()
        self.transaction_stack = Stack()

    def issueBook(self, book_id):
        book = self.book_list.searchBook(book_id)
        if book and book.status == "Available":
            book.status = "Issued"
            self.transaction_stack.push(("issue", book_id))
            print(f"Book '{book.title}' issued successfully.\n")
        elif book:
            print("Book is already issued.\n")

    def returnBook(self, book_id):
        book = self.book_list.searchBook(book_id)
        if book and book.status == "Issued":
            book.status = "Available"
            self.transaction_stack.push(("return", book_id))
            print(f"Book '{book.title}' returned successfully.\n")
        elif book:
            print("Book is not issued yet.\n")

    def undoTransaction(self):
        last = self.transaction_stack.pop()
        if not last:
            print("No transaction to undo.\n")
            return
        action, book_id = last
        book = self.book_list.searchBook(book_id)
        if action == "issue":
            book.status = "Available"
            print(f"Undo Successful → Book '{book.title}' is now Available again.\n")
        elif action == "return":
            book.status = "Issued"
            print(f"Undo Successful → Book '{book.title}' is now Issued again.\n")

    def viewTransactions(self):
        self.transaction_stack.display
        
if __name__ == "__main__":
    system = LibrarySystem()

    while True:
        print("=== Library Book Management System ===")
        print("1. Insert Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Undo Last Transaction")
        print("8. View Transactions")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            bid = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            system.book_list.insertBook(bid, title, author)

        elif choice == '2':
            bid = int(input("Enter Book ID to delete: "))
            system.book_list.deleteBook(bid)

        elif choice == '3':
            bid = int(input("Enter Book ID to search: "))
            system.book_list.searchBook(bid)

        elif choice == '4':
            system.book_list.display

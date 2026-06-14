class Book:
    def __init__(self,author,title):
        self.author = author
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(self.title , "has been borrowed")
        else:
           print(self.title , "has alrady been borrowed")
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(self.title , "has been returned")
        else:
            print(self.title , "has not been borrowed")
book1 = Book("Of mice and men" , "nandinii")
book2 = Book("that is not my favourite book" , "shariq")
book3 = Book("macbeth" , "shakepeare")
book1.borrow()
book2.borrow()
book3.borrow()
print()
book1.return_book()
book2.return_book()
book3.return_book()
print()
book1.borrow()
book1.borrow()
print()
book1.return_book()
book1.return_book()



from food import food

class food_operations:

    foodlist = []

    def add_food(self):
        print("*********Add food*******")
        foodID = int(input("enter the Food Id :"))
        Name = input("enter the food name :")
        Quantity = input ("enter the quantity of food :")
        Price = int(input("enter the price of food :"))
        print("Successfully Added")

    def view_food(self):
        print("*********All Books*******")
        for books in self.booklist:
            print(books,"\n")

    def file_reading(self):       
        file = open("food.txt")
        data = file.read()
        print(data)

    def delete_book(self):
        print("*******Delete Book******")
        try:
            book_ID = int(input("Enter book ID : "))
            book = self.search_book_by_ID(book_ID)
            if book:
                self.booklist.remove(book)
                print("Successfully Deleted")
        except Exception as ex:
            print(ex)

    def update_book(self):
        print("*******Update Book*******")
        book_ID = int(input("Enter book ID : "))
        book = self.search_book_by_ID(book_ID)
        if book:
            book_name = input("Enter book name : ")
            book_edition = int(input("Enter book edition : "))
            book_author = input("Enter book author : ")
            book_publication = input("Enter book publication : ")
            book_price = float(input("Enter book price : "))

            book.set_book_name(book_name)
            book.set_book_edition(book_edition)
            book.set_book_author(book_author)
            book.set_book_publication(book_publication)
            book.set_book_price(book_price)

            print("Successfully Updated")
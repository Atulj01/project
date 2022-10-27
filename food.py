
from dis import disco


class food():
    def __init__(self,foodID,Name,Quantity,price):
        self.__foodID = foodID
        self.__Name = Name
        self.__Quantity = Quantity
        self.__price = price
    

    def __str__(self):
      
        return f"FoodID : {self.__foodID}, Food Name : {self.__Name}, Quantity :{self.__Quantity}, Price : {self.__price},"
        

    def set_foodID(self,foodID):
        self.__foodID = foodID

    def get_foodID(self):
        return self.__foodID

    def set_Name(self,Name):
        self.__Name = Name

    def get_Name(self):
        return self.__Name

    def set_Quantity(self,Quantity):
        self.__Quantity = Quantity

    def get_Quantity(self):
        return self.__Quantity

    def set_price(self,price):
        self.__price = price

    def get_price(self):
        return self.__price

if __name__ == "__main__":
    food_obj = food( 1, "Paneer" ,"1 plate" , "200")
    print(food_obj)

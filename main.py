from food_operations import food_operations

class main_class:

    def file_reading(self):       
        file = open("G:\python practies\food_app.py\mini_project\food.txt")
        data = file.read()
        print(data)


    def __init__(self):
        self.food_operations = food_operations()

    def execute(self,choice):
        if choice == 1:
            self.food_operations.add_food()
        elif choice == 2:
            self.food_operations.view_food()
        elif choice == 3:
            food_ID = int(input("Enter food ID : "))
            food = self.food_operations.search_food_by_ID(food_ID)
            print(food)
        elif choice == 4:
            self.food_operations.delete_food()
        elif choice == 5:
            self.food_operations.update_food()
        
if __name__ == "__main__":
    
    obj = main_class()

    while True:
        choice = int(input("Enter \n1.Add food \n2.View food \n3.Search food By ID \n4.Delete food \n5.Update food : \n"))
        if choice > 5 or choice < 1:
            break
        obj.execute(choice)

    

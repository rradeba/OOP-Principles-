# Task 1 

#create class 
class  BudgetCategory:
    def __init__(self, category_name, allocated_budget, deduction_amount):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget 
        self.__deduction_amount = deduction_amount  
        
    def name_getter(self):
        return self.__category_name 

#global new_amount variable to be referenced in print ing function
    new_amount = 0 
    
#category name setter 
    def name_setter(self, category_name):
        self.__category_name = category_name


#allocated budget getter  
    def budget_getter(self):
        return self.__allocated_budget
    
#allocated budget setter 
    def budget_setter(self, allocated_budget): 
            if allocated_budget <= 0:
                self.__allocated_budget = allocated_budget
            else: 
                raise ValueError("Balance must be positive or zero.")
                     
                     
# method for adding  expenses for a catgory
    def add_expense(self):
        global new_amount 
        if self.__deduction_amount > 0:   
            new_amount = self.__allocated_budget
            new_amount -= self.__deduction_amount
            return  new_amount 
        else:
            raise ValueError("Deposit amount must be positive")

#display category information 
    def look_category(self):
        print(f"--------------------------\nCategory: {self.__category_name}")
        print(f"Budget: ${self.__allocated_budget}")
        print(f"Deduction amount: ${self.__deduction_amount}")
        print(f"Amount left: ${new_amount}\n--------------------------")
        

#connect food category variable to object and reference the 
food_category = BudgetCategory("Food", 1000, 100)
food_category.add_expense()
food_category.look_category()


#connect subscriptions category variable to object and reference the 
sub_category = BudgetCategory("Subscriptions", 100, 50)
sub_category.add_expense()
sub_category.look_category()










# Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, focusing on the use of private attributes and getters and setters.

# Problem Statement: You are required to build a Personal Budget Management application. 
# The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.



# Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget. - Initialize these attributes in the constructor.

# - Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

# Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. - Ensure that the setter methods include validation (e.g., budget should be a positive number).

# - Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

# Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust the budget accordingly. - Validate the expense amount before making deductions from the budget.

# Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

# Task 4: Display Budget Details Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.

# Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action
import add_expense
import display

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, category_name):
        self.__category_name = category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
        else:
            print("Invalid budget amount.")

    def get_remaining_budget(self):
        return self.__remaining_budget

    def set_remaining_budget(self, remaining_budget):
        self.__remaining_budget = remaining_budget

    def add_expense(self, expense):
        if expense > 0 and expense <= self.__remaining_budget:
            self.__remaining_budget -= expense
            print("Expense added successfully.")
        else:
            print("Invalid expense amount.")

    def display_budget_details(self):
        print("Category Name:", self.__category_name)
        print("Allocated Budget:", self.__allocated_budget)
        print("Remaining Budget:", self.__remaining_budget)
        
# Create instances of BudgetCategory

food_category = BudgetCategory("Food", 500)
entertainment_category = BudgetCategory("Entertainment", 300)

# Add expenses to the categories
food_category.add_expense(100)
entertainment_category.add_expense(50)

# Display budget details

food_category.display_budget_details()

entertainment_category.display_budget_details()

# Modify budget details

food_category.set_allocated_budget(600)

food_category.display_budget_details()

# Modify budget details

entertainment_category.set_remaining_budget(200)

entertainment_category.display_budget_details()

# Modify budget details

entertainment_category.set_allocated_budget(400)

entertainment_category.display_budget_details()

# Modify budget details

entertainment_category.set_allocated_budget(-400)

entertainment_category.display_budget_details()

# Modify budget details

entertainment_category.set_remaining_budget(-200)

entertainment_category.display_budget_details()

        
        
      
   



    


            
            
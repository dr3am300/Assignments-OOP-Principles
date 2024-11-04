import Budget

def add_expense(self, expense):
        if expense > 0 and expense <= self.__remaining_budget:
            self.__remaining_budget -= expense
            print("Expense added successfully.")
        else:
            print("Invalid expense amount.")
            
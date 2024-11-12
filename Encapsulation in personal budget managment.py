class BudgetCategory:
    def __init__(self, name, allocated_budget):
        self.__name = name
        self.__allocated_budget = allocated_budget
        self.expenses_total = 0  
    def get_name(self):
        return self.__name
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_name(self, new_name):
        self.__name = new_name

    def set_allocated_budget(self, new_budget):
        self.__allocated_budget = new_budget
    
    def add_budget(self, amount):
        if amount > 0:
            self.set_allocated_budget(self.get_allocated_budget() + amount)
            print(f"Added: {amount}")
        else:
            print("Amount couldn't be added")

    def add_expense(self, amount):  
        if amount <= self.get_allocated_budget() - self.expenses_total:
            self.expenses_total += amount
            print(f"{amount} has been subtracted from budget!")
        else:
            print("Insufficient funds")
    
    def display_budget_details(self):
        remaining_budget = self.__allocated_budget - self.expenses_total
        print(f"Receipt: {self.__name} | Budget: {self.__allocated_budget} | Remaining Budget After Expenses: {remaining_budget}")


budget1 = BudgetCategory("Donald", 1000)

budget1.add_budget(150)
budget1.add_expense(250)
budget1.display_budget_details()

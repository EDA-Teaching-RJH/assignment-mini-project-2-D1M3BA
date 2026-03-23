class Transaction:
    def __init__(self, amount, description, category, date):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = date


    def __str__(self):
        return f"{self.date} | {self.description} | {self.category} | £{self.amount}"
    
class Expense(Transaction):
    type = "expense"
    def __init__(self, amount, description, category, date):
        super().__init__(amount, description, category, date)


class Income(Transaction):
    type = "income"
    def __init__(self, amount, description, category, date):
        super().__init__(amount, description, category, date)
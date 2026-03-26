import sys
import csv
import re
import matplotlib.pyplot as plt
from classes import Transaction, Expense, Income
from utils import get_amount, get_date, get_description, sort_by_category, sort_by_date, sort_by_price, print_transactions, select_transaction

def main():
    """Checks if there are enough command line arguments, initialises the file and loads its data into memory. Runs the main menu loop until the user exits."""
    if len(sys.argv)  != 3:
        print("Usage: personalExpenseTracker.py <create|open> <filename> ")
        sys.exit()

    filename = sys.argv[2]
    mode = sys.argv[1]

    init_file(filename, mode)
    transactions = load_transactions(filename)
    categories = load_categories(filename)

    while True:
        print_menu()
        while True:
            opt = get_opt()
            if opt in ["0", "1", "2", "3", "4", "5", "6"]:
                break
            else:
                print("Invalid option, please try again!")
            
        if opt == "0" :
            print(f"See you next time")
            sys.exit()
        elif opt =="1":
            view_transactions(transactions)
        elif  opt =="2":
            categories, transactions = get_transaction(filename, categories, transactions)
        elif opt == "3":
            categories, transactions = alter_transaction(filename, categories, transactions)
        elif opt == "4":
            categories, transactions = categories_menu(filename,categories, transactions)
        elif opt == "5":
            print(f"Your balance is {get_balance(transactions)}")
        elif opt == "6":
            plot_menu(transactions)


def plot_menu(transactions):
    """The menu for plotting graphs, prompts the user to select a graph type and plots that graph."""
    print("1.Spending by category ")
    print("2.Spending over time ")
    print("3.Income vs expense")
    while True:
        opt = get_opt()
        if opt in ["1", "2", "3"]:
            break
        else:
            print("Invalid input, please try again")
    if opt == "1":
       plot_by_category(transactions)
    elif opt == "3":
        plot_income_vs_expense(transactions)
    else:
       plot_spending_over_time(transactions)

def plot_spending_over_time(transactions):
    """Sorts the transactions by date. Then extracts the date and amount attributes from the expense subclass and stores them into lists. Then plots dates against amounts."""
    sorted_t = sort_by_date(transactions)
    dates = []
    amounts = []
    for i in range(len(sorted_t)):
        if sorted_t[i].type == "expense":
            dates.append(sorted_t[i].date)
            amounts.append(sorted_t[i].amount)

    plt.plot(dates, amounts, marker="o")
    plt.title("Spending Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount £")
    plt.xticks(rotation=45)  
    plt.tight_layout()       
    plt.show()

def plot_by_category(transactions):
    """Loops over transactions and checks if a category is currently being tracked. If not, it stores it in a list and uses a parallel list to associate amounts with categories. If the category is being tracked it finds the correct index and sums the amounts. Then plots a bar chart using that data."""
    categories = []
    amounts = []
    for t in transactions:
        if t.type == "expense":
            if t.category in categories:
                idx = categories.index(t.category)
                amounts[idx] += t.amount
            else:
                categories.append(t.category)
                amounts.append(t.amount)
    
    plt.bar(categories, amounts)
    plt.title("Spending by Category")
    plt.show()

def plot_income_vs_expense(transactions):
    """Loops over transactions and checks the transaction type, income or expense. It then sums the amounts belonging to each subclass. Then plots it in a pie chart."""
    income = 0
    expenses = 0
    for i in range(len(transactions)):
        if transactions[i].type == "income":
            income += transactions[i].amount
        else:
            expenses += transactions[i].amount

    plt.pie([expenses, income], labels=["Expenses", "Income"], autopct="%1.1f%%")
    plt.title("Income vs Expenses")
    plt.show()
    


def get_balance(transactions):
    """Loops over transactions and checks the transaction type, income or expense. It then sums the amounts belonging to each subclass. Then uses those totals to calculate a balance, rounded to two decimal places."""
    expense = 0
    income= 0 
    for i in range(len(transactions)):
        if transactions[i].type  == "expense":
            expense += transactions[i].amount
        elif transactions[i].type == "income":
            income +=  transactions[i].amount 

    return round(income - expense, 2)





def categories_menu(filename, categories, transactions):
    """Menu for categories. Prompts the user for input and performs different actions depending on the selection."""
    print("1. Add a category")
    print("2. Change a category ")
    print("3. View categories")
    while True:
        opt = get_opt()
        if opt in ["1", "2", "3"]:
            break
        else:
            print("Invalid input, please try again")
    if opt == "1":
      categories =  add_category(categories)
    elif opt == "3":
        view_category(categories)
    elif opt == "2":
       categories, transactions = edit_category(filename, categories, transactions)
    
    return categories, transactions


def view_category(categories):
    """Iterates over categories and prints each one in a numbered list."""
    for i in range(len(categories)):
        print(f"{i+1}. {categories[i]}")


def edit_category(filename, categories, transactions):
    """Prints the current list of categories so the user can see them. Prompts the user to select a category by entering its associated number. Stores the old category for reference. Prompts the user to use an existing category or create a new one. Iterates over transactions using the reference to find matching categories and updates them. Then saves to the CSV."""
    view_category(categories)
    
    while True:
        try:
            idx = int(input("Select category to edit: ")) - 1
            if 0 <= idx < len(categories):
                break
            print("Invalid number")
        except ValueError:
            print("Enter a number")

    old_category = categories[idx]
    
    print(f"Editing: {old_category}")
    print("1. Change to existing category")
    print("2. Create new category")
    
    while True:
        opt = get_opt()
        if opt in ["1", "2"]:
            break
        print("Invalid option")

    if opt == "1":
        new_category = get_category(categories)[0]
    elif opt == "2":
        new_category = input("Enter new category name: ")
        categories.append(new_category)

    for i in range(len(transactions)):
        if transactions[i].category == old_category:
            transactions[i].category = new_category
    
    categories.remove(old_category)
    save_transactions(filename, transactions)
    return categories, transactions

def add_category(categories):
    """Prompts the user to enter a new category name. Appends it to the categories list if it doesn't already exist."""
    new_category = input("Enter new category name: ")
    if new_category not in categories:
        categories.append(new_category)
    return categories


def view_transactions(transactions):
    """Prompts the user to select how they want to view transactions. Sorts transactions based on that choice and prints a formatted list."""
    print ("How would you like to view the transactions")
    print ("1. As they are now")
    print ("2. Sorted by date")
    print ("3. Sorted by price")
    print ("4. Sorted by Category")
    print ("5. Exit to menu")
    while True:
            opt = get_opt()
            if opt in ["1", "2", "3", "4", "5"]:
                break
            else:
                print("Invalid option, please try again!")
    if opt == "5":
        return
    elif opt == "1":
        print_transactions(transactions)
    elif opt == "2":
        print_transactions(sort_by_date(transactions))
    elif opt == "3":
        print_transactions(sort_by_price(transactions))
    elif opt == "4":
        print_transactions(sort_by_category(transactions))
    

    

def alter_transaction(filename, categories, transactions):
    """Menu for altering transactions. Prompts the user to select edit or delete. Then prompts the user to select a transaction and proceeds accordingly."""
    print("Would you like to?")
    print ("1. Edit a transaction")
    print ("2. Remove a transaction")
    print ("3. Cancel edit")
    while True:
        opt = get_opt()
        if opt in ["1", "2", "3"]:
            break
        else:
            print("Invalid option, please try again!")
    if opt == "3":
        return categories, transactions
    elif opt == "1":
        idx  =  select_transaction(transactions, "edit")
        edit_transaction(transactions, idx, filename, categories)
    elif opt == "2":
        idx = select_transaction(transactions, "delete" )
        delete_transactions(filename, transactions,idx)
    return categories, transactions
            
            

def edit_transaction(transactions, idx, filename, categories):
    """Continually asks the user which attribute they want to change until they exit. Uses the index passed in to directly alter that specific attribute. Saves all transactions to the CSV when done."""
    print(f"Editing: {transactions[idx]} | {transactions[idx].type}")
    
    while True:
        print("1. Date")
        print("2. Description")
        print("3. Category")
        print("4. Amount")
        print("5. Done editing")

        while True:
            opt = get_opt()
            if opt in ["1", "2", "3", "4", "5"]:
                break
            print("Invalid option")

        if opt == "1":
            transactions[idx].date = get_date()
        elif opt == "2":
            transactions[idx].description = get_description()
        elif opt == "3":
            transactions[idx].category = get_category(categories)[0]
        elif opt == "4":
            transactions[idx].amount = float(get_amount())
        elif opt == "5":
            break

    save_transactions(filename, transactions)
    return transactions

def delete_transactions(filename, transactions, idx):
    """Removes the transaction at the selected index and saves the updated list to the CSV."""
    transactions.pop(idx)
    save_transactions(filename, transactions)
    return transactions   

            
def save_transactions(filename, transactions):
    "Opens the CSV in write mode, completely overwriting the previous contents. Writes the headers then writes each transaction from the current transactions list."      
    with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["amount", "description", "category", "date", "type"])
            for t in transactions:
                writer.writerow([t.amount, t.description, t.category, t.date, t.type])


def load_transactions(filename):
    """Opens the CSV in read mode and skips the header. Checks the transaction type and creates the appropriate subclass, associating each column with the correct attribute in the constructor."""
    transactions = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            if row[4] == "income":
                t = Income(float(row[0]), row[1], row[2], row[3])
            else:
                t = Expense(float(row[0]), row[1], row[2], row[3])
            transactions.append(t)
    return transactions


def load_categories(filename):
    """Opens the CSV in read mode and skips the header. Appends the category column data to a list row by row, checking for uniqueness """
    categories = []  
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            if row:
                if row[2] not in categories:
                    categories.append(row[2])
    return categories   




def init_file(filename, mode):
    """Checks if the filetype is appropriate, exits if not. Checks the mode then creates or opens a file accordingly. If the mode is unrecognised it prints correct usage and exits"""
    if not validate_file_type(filename):
            print("Error: file must be a .csv")
            sys.exit()


    if mode.lower() == "create":
        
        create_file(filename)

    elif mode.lower() == "open":

        if not validate_file(filename):
            print("Error: Invalid file")
            sys.exit()
        else:
            print(f"Sucessfully opened {filename} ")
    
    else: 
        
        print("Usage: personalExpenseTracker.py  <create|open> <filename>")
        sys.exit()

def get_transaction(filename, categories, transactions):
    """Prompts the user for transaction type then collects each attribute. Creates the appropriate subclass using the constructor, appends it to the transactions list and writes it to the file."""
    print("What sort of transaction would you like to record?")
    print("1. Expense")
    print("2. Income")
    print("3. Cancel transaction")
    while True:
        opt = get_opt()
        if opt in ["1", "2", "3"]:
            break
        else:
            print("Invalid option, please try again!")
        
    if opt == "3":
        return categories, transactions
    
    amount = get_amount()
    date = get_date()
    description = get_description()
    
    category, categories = get_category(categories)
    if opt == "1":
         t = Expense(float(amount), description, category, date)
    elif opt ==  "2":
         t = Income(float(amount), description, category, date)
    transactions.append(t)
    append_transaction(filename , t)

    return categories, transactions   

def append_transaction(filename, t):
    """Takes a transaction object and appends a row to the file with each attribute in the correct column."""
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([t.amount, t.description, t.category, t.date, t.type])


def get_category(categories):
        """Prompts the user for a category. If it exists in the list it returns it. If not, asks the user if they would like to create it. If yes, updates the categories list and returns the new category"""
        while True:
            category = input("Enter the transaction category: ")
            if category in categories:
                return category, categories
            else:
                print(f"The category: {category} does not exists would you like to add it y/n")
                while True:
                    opt = get_opt()
                    if opt in ["y", "n"]:
                        break
                    else: 
                        print("Invalid option, try y or n ")
                if opt == "y":
                    categories.append(category)
                    return category, categories
                if opt == "n":
                    pass
                    
                

            
   
        

def get_opt():
    "Prompts for input and returns it."
    return input("Enter your option: ")
    
    
def print_menu():
    """Prints the main menu options."""
    print("1. View transactions")
    print("2. Add a Transaction")
    print("3. Edit Transactions")
    print("4. Categories")
    print("5. View balance")
    print("6. Plot graphs")
    print("0. Exit the program")
    
    



        

def validate_file_type(filename):
    """ Uses regex to validate that the file is a CSV."""
    if not re.match(r".+\.csv$", filename):
            return False
    return True 


def validate_file(filename):
    """OOpens the file in read mode and checks if the first row matches the expected headers. Returns True if valid, False otherwise. If the file cannot be opened it notifies the user and returns False."""
    HEADERS = ["amount", "description", "category", "date", "type"]
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            headers = next(reader, None)
            if headers is None or headers != HEADERS:
                print("Invalid file")
                return False
            return True
    except FileNotFoundError:
        print("File not found.")
        return False
        



def create_file(filename):
    """Tries to open the file. If successful, asks the user if they wish to overwrite it. If yes, creates the file in write mode with the correct headers. If no, exits the program."""
    try:
         with open(filename, "r"):
            while True:
                overwrite = input(f"{filename} already exists do you want to overwrite it? y/n")
                if overwrite == "y":
                    break
                elif overwrite == "n":
                    sys.exit()
                else:
                    print("Invalid input, try y/n")  
    except FileNotFoundError:
         pass

          
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["amount", "description", "category", "date", "type"])
    






if __name__ == "__main__":
    main()




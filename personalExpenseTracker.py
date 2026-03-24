import sys
import csv
import re
from classes import Transaction, Expense, Income
from utils import get_amount, get_date, get_description

def main():
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
            if opt in ["0", "1"]:
                break
            else:
                print("Invalid option, please try again!")
            
        if opt == "0" :
            print(f"See you next time")
            sys.exit()
        elif  opt =="1":
            categories, transactions = get_transaction(filename, categories, transactions)

def load_transactions(filename):
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
    save_transaction(filename , t)

    return categories, transactions   

def save_transaction(filename, t):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([t.amount, t.description, t.category, t.date, t.type])


def get_category(categories):
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
    return input("Enter your option: ")
    
    
def print_menu():

    print("1. Add a Transaction")
    print("0. Exit the program")



        

def validate_file_type(filename):
    if not re.match(r".+\.csv$", filename):
            return False
    return True 


def validate_file(filename):
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




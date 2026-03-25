import re
from datetime import datetime
from classes import Transaction, Income, Expense


def get_amount():
    while True:
        amount = input("Enter the value of the transaction: ")
        if validate_amount(amount):
            return amount
        print("Invalid amount, e.g 32 or 32.32")

def validate_amount(amount):
    return bool(re.match(r"^\d+(\.\d{2})?$", amount))



def get_date():
    while True:
        date = input("Enter the date (DD/MM/YYYY): ")
        if validate_date(date):
            return date
        print("Invalid date, e.g 01/01/2000")

def validate_date(date):
    return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", date))

def get_description():
    while True:
        description = input("Enter description: ")
        if validate_description(description):
            return description
        print("Invalid description, only alpha numerical characters")

def validate_description(description):
    return bool(re.match(r"^[a-zA-Z0-9\s]+$", description))




def sort_by_date(transactions):
    return sorted(transactions, key=lambda t: datetime.strptime(t.date, "%d/%m/%Y"))

def sort_by_category(transactions):
    return sorted(transactions, key=lambda t: (t.category, datetime.strptime(t.date, "%d/%m/%Y")))

def sort_by_price(transactions):
    return sorted(transactions, key=lambda t: t.amount)


def print_transactions(transactions):
    if not transactions:
        print("Nothing to display")
        return
    
    print(f"{'#':<5} {'Date':<12} {'Description':<20} {'Category':<15} {'Amount':>10} {'Type':<20}")
    print("-" * 70)
    n = 1
    for t in transactions:
        if len(t.description) > 20:
            description = t.description[:17] + "..." 
        else:
            description = t.description

        print(f"{n:<5} {t.date:<12} {description:<20} {t.category:<15} {t.amount:>10.2f} {t.type:<20}")
        n += 1


def select_transaction(transactions, mode):
    print(f"Which transaction would you like to {mode}, select one from below")
    print_transactions(transactions)
    while True:
        try:
            index = int(input("Select transaction number: "))
            if 1 <= index <= len(transactions):
                return (index - 1)
            print("Invalid number, try again")
        except ValueError:
            print("Enter a number")



    
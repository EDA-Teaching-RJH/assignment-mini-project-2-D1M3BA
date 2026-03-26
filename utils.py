import re
from datetime import datetime
from classes import Transaction, Income, Expense


def get_amount():
    """Prompts the user for input. Checks if the input is valid and returns it if it is."""
    while True:
        amount = input("Enter the value of the transaction: ")
        if validate_amount(amount):
            return amount
        print("Invalid amount, e.g 32 or 32.32")

def validate_amount(amount):
    """Checks if all characters are digits. If there is a decimal point, it checks that it's followed by exactly 2 digits. Returns True or False based on the check."""
    return bool(re.match(r"^\d+(\.\d{2})?$", amount))


def get_date():
    """Prompts the user for input. Checks if the input is valid and returns it if it is."""
    while True:
        date = input("Enter the date (DD/MM/YYYY): ")
        if validate_date(date):
            return date
        print("Invalid date, e.g 01/01/2000")

def validate_date(date):
    """Returns True if the date is comprised of 2 digits followed by a slash, 2 more digits, a slash, and then 4 digits. Returns False if not."""
    return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", date))


def get_description():
    """Prompts the user for input. Checks if the input is valid and returns it if it is."""
    while True:
        description = input("Enter description: ")
        if validate_description(description):
            return description
        print("Invalid description, only alpha numerical characters")

def validate_description(description):
    """Checks if the description contains only alphanumeric characters and spaces. Returns True or False based on the check."""
    return bool(re.match(r"^[a-zA-Z0-9\s]+$", description))


def sort_by_date(transactions):
    """For each transaction in the list, the lambda extracts the date string and converts it into a datetime object. This is then used to sort the transactions list chronologically."""
    return sorted(transactions, key=lambda t: datetime.strptime(t.date, "%d/%m/%Y"))

def sort_by_category(transactions):
    """For each transaction in the list, the lambda extracts the category and sorts the transactions alphabetically. It also extracts the datetime objects and uses them for tiebreakers inside categories."""
    return sorted(transactions, key=lambda t: (t.category, datetime.strptime(t.date, "%d/%m/%Y")))

def sort_by_price(transactions):
    """For each transaction in the list, the lambda extracts the amount and then sorts transactions from smallest to biggest."""
    return sorted(transactions, key=lambda t: t.amount)


def print_transactions(transactions):
    """If the list of transactions is empty, it prints 'Nothing to display'. If not, it prints the transactions, formatting everything with f-strings to ensure spacing is consistent and aligned properly across columns."""
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
    """Prints a list of transactions so the user can choose one. Prompts the user for a choice, then returns the index of that choice in the transactions list."""
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
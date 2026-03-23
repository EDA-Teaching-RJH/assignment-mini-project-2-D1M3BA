import re

def get_amount():
    while True:
        amount = input("Enter the value of the transaction: ")
        if re.match(r"^\d+(\.\d{2})?$", amount):
            return amount
        print("Invalid amount, e.g 32 or 32.32")

def get_date():
    while True:
        date = input("Enter the date (DD/MM/YYYY): ")
        if re.match(r"^\d{2}/\d{2}/\d{4}$", date):
            return date
        print("Invalid date, e.g 01/01/2000")

def get_description():
    while True:
        description = input("Enter description: ")
        if re.match(r"^[a-zA-Z0-9\s]+$", description):
            return description
        print("Invalid description, only alpha numerical characters")
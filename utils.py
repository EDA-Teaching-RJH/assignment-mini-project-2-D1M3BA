import re



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


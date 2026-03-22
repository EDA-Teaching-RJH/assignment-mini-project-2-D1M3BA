import sys
import csv
import re
from classes import Transaction, Expense, Income

def main():
    if len(sys.argv)  != 3:
        print("Usage: personalExpenseTracker.py <create|open> <filename> ")
        sys.exit()

    filename = sys.argv[2]
    mode = sys.argv[1]

    if not validate_file_type(filename):
            print("Error: file must be a .csv")
            sys.exit()


    if mode.lower() == "create":
        
        create_file(filename)

    elif mode.lower() == "open":

        if not validate_file(filename):
            print("Error: Invalid file")
            sys.exit
        else:
            print(f"Sucessfully opened {filename} ")
    
    else: 
        
        print("Usage: personalExpenseTracker.py  <create|open> <filename>")
        sys.exit()

    while True:
        print_menu()
        while True:
            opt = get_opt()
            if opt in ["0"]:
                break
            else:
                print("Invalid option, please try again!")
            
        if opt == "0" :
            print(f"See you next time")
            sys.exit()
def get_opt():
    return input("Enter your option: ")
    
    
def print_menu():

    print("0. Exit the program")



        

def validate_file_type(filename):
    if not re.match(r".+\.csv$", filename):
            return False
    return True 


def validate_file(filename):
    HEADERS = ["amount", "description", "category", "date"]
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
        writer.writerow(["amount", "description", "category", "date"])
    


if __name__ == "__main__":

    main()




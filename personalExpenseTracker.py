import sys
import csv
import re


def main():
    if len(sys.argv)  != 3:
        print("Usage: python main.py <filename> <create|open>")
        sys.exit()

    filename = sys.argv[1]
    mode = sys.argv[2]

    if not validate_file_type(filename):
            print("Error: file must be a .csv")
            sys.exit()


    if mode.lower() == "create":
        
        create_file(filename)

    elif mode.lower() == "open":

        validate_file(filename)
    
    else: 
        
        print("Usage: python main.py <filename> <create|find>")
        sys.exit()

        

def validate_file_type(filename):
    if not re.match(r".+\.csv$", filename):
            return False
    return True 


def validate_file(filename):
    HEADERS = ["amount", "description", "category", "date"]
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            if headers != HEADERS:
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
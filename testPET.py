import unittest
import csv
import os
from personalExpenseTracker import validate_file_type, validate_file,save_transaction, load_transactions
from utils import validate_description, validate_amount, validate_date
from classes import Transaction, Income, Expense

class TestValidateFileType(unittest.TestCase):
    def test_valid_csv(self):
        self.assertTrue(validate_file_type("transactions.csv"))

    

    def test_invalid_csv(self):
        self.assertFalse(validate_file_type("transcations.txt"))

    

    def test_no_extension(self):
        self.assertFalse(validate_file_type("transactions"))


    

    def test_csv_wrong_format_one(self):
        self.assertFalse(validate_file_type(".csv.transactions"))

    

    def test_invalid_csv_two(self):
        self.assertFalse(validate_file_type("tansactions.csvs"))

    

    def test_csv_wrong_format_two(self):
        self.assertFalse(validate_file_type("trans.csv actions"))




    def test_empty_string(self):
        self.assertFalse(validate_file_type(""))


    

class TestValidateFile(unittest.TestCase):
    def setUp(self):
        with open("test_valid.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["amount", "description", "category", "date", "type"])
    
        with open("incorrect_headers.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["These", "Headers", "are", "wrong"])
    
        with open("too_many_headers.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["amount", "description", "category", "date", "hi", "bye"])
    
        with open("headers_wrong_order.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["amount", "date", "category", "description", "type"])

   
        with open("emptyfile.csv", "w") as f:
            pass

    def test_valid_file(self):
        self.assertTrue(validate_file("test_valid.csv"))
    
    def test_incorrect_headers(self):
        self.assertFalse(validate_file("incorrect_headers.csv"))

    def test_too_many_headers(self):
        self.assertFalse(validate_file("too_many_headers.csv"))
    
    def test_headers_wrong_order(self):
        self.assertFalse(validate_file("headers_wrong_order.csv"))

    def test_empty_file(self):
        self.assertFalse(validate_file("emptyfile.csv"))
        


    
    def test_file_not_found(self):
        self.assertFalse(validate_file("doesnotexist.csv"))
    
    def tearDown(self):
        for file in ["test_valid.csv", "incorrect_headers.csv", "too_many_headers.csv", "headers_wrong_order.csv", "emptyfile.csv"]:
            if os.path.exists(file):
                os.remove(file)


class TestLoadTransactions(unittest.TestCase):
    
    def setUp(self):
        with open("test_load.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["amount", "description", "category", "date", "type"])
            writer.writerow([50.00, "Tesco", "food", "01/01/1900", "expense"])
            writer.writerow([1000.00, "Salary", "work", "01/01/2000", "income"])

    def test_loads_correct_types(self):
        transactions = load_transactions("test_load.csv")
        self.assertIsInstance(transactions[0], Expense)
        self.assertIsInstance(transactions[1], Income)

    def test_loads_correct_values(self):
        transactions = load_transactions("test_load.csv")
        self.assertEqual(transactions[0].amount, 50.00)
        self.assertEqual(transactions[1].description, "Salary")

    def tearDown(self):
        if os.path.exists("test_load.csv"):
            os.remove("test_load.csv")

   
    
class TestValidators(unittest.TestCase):
    def test_valid_amount(self):
        self.assertTrue(validate_amount("50.00"))
    
    def test_invalid_amount(self):
        self.assertFalse(validate_amount("abc"))
    
    def test_valid_date(self):
        self.assertTrue(validate_date("01/01/2000"))
    
    def test_invalid_date(self):
        self.assertFalse(validate_date("201/011/200"))


class TestSaveTransaction(unittest.TestCase):
    
    def setUp(self):
        with open("test_save.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["amount", "description", "category", "date", "type"])

    def test_saves_expense(self):
        t = Expense(50.00, "Tesco", "food", "01/01/2000")
        save_transaction("test_save.csv", t)
        
        with open("test_save.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)  
            row = next(reader) 
        
        self.assertEqual(float(row[0]), 50.00)
        self.assertEqual(row[1], "Tesco")
        self.assertEqual(row[2], "food")
        self.assertEqual(row[3], "01/01/2000")
        self.assertEqual(row[4], "expense")

    def test_saves_income(self):
        t = Income(1000.00, "Salary", "work", "01/01/2000")
        save_transaction("test_save.csv", t)
        
        with open("test_save.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)
            row = next(reader)
        
        self.assertEqual(row[4], "income")

    def tearDown(self):
        if os.path.exists("test_save.csv"):
            os.remove("test_save.csv")





if __name__ == "__main__":
    unittest.main()


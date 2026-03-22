import unittest
import csv
from personalExpenseTracker import validate_file_type, validate_file

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
            writer.writerow(["amount", "description", "category", "date"])
    
        with open("incorrect_headers.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["These", "Headers", "are", "wrong"])
    
        with open("too_many_headers.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["amount", "description", "category", "date", "hi"])
    
        with open("headers_wrong_order.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["amount", "date", "category", "description"])

   
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
    



if __name__ == "__main__":
    unittest.main()
import unittest
from csvfile import CSVFile


class Test_CSVFile(unittest.TestCase):
    def test_init(self):
        csv_file = CSVFile('shampoo_sales.csv')
        #controllo che il nome del file sia stato salvato in un attributo dell'oggetto di nome "name"
        self.assertEqual(csv_file.name, 'shampoo_sales.csv')

    def test_get_data(self):
       csv_file = CSVFile('shampoo_sales.csv')
       Expectation = [['01-01-2012\n'], ['01-01-2012', 'ciao\n']]
       self.assertEqual(csv_file.get_data(0,2), Expectation)
       
    def test_file_less(self):
        with self.assertRaises(Exception):
            csv_file = CSVFile('shampoo_sales.csv')
            csv_file.get_data(25, 1)

    def test_isinstance(self):
        with self.assertRaises(Exception):
            csv_file = CSVFile('shampoo_sales.csv')
            csv_file.get_data (1.5,2)
    

    
    




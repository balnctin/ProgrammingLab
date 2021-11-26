class CSVFile():
  def __init__ (self, name):
      self.name = name
      print('Name: {}'.format(self.name))
  def get_data(self):
      data = []
      try:
          my_file = open(self.name, 'r')

          for line in my_file:
              elements = line.split (',')
              if elements[0]!='Date':
                  data.append(elements)
          my_file.close()
          return data
      except Exception as e:
        print('Non posso aprire "my_file"')
        print('Non posso aprire un file non esistente: {}'.format(e))

my_file = CSVFile("shampoo_sales.csv")
print('Dati nel file: {}'.format(my_file.get_data()))
#supergetdata


class NumericalCSVFile(CSVFile):
  def __init__ (self, name):
      self.name = name
      print('Name: {}'.format(self.name))
  def get_data(self):
      data = super().get_data()
      values = []
      for my_list in data:
        for item in my_list:
          try:
            item = float(item)
            values.append(item)
          except:
            print('Non posso convertire: {}'.format(item))
            
      return values
my_file = NumericalCSVFile("shampoo_sales.csv")
print('Dati: {}'.format(my_file.get_data()))
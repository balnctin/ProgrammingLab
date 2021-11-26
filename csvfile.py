class CSVFile():
  def __init__ (self, name):
      self.name = name
      print('Name: {}'.format(self.name))
  def get_data(self):
      data = []
      my_file = open(self.name, 'r')
      for line in my_file:
          elements = line.split (',')
          if elements[0]!='Date':
              data.append(elements)
          
      my_file.close()
      return data

my_file = CSVFile("shampoo_sales.csv")
print('Dati nel file: {}'.format(my_file.get_data()))

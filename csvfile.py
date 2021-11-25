class CSVFile():
  def __init__ (self, name):
      self.name = name
  def get_data(self):
      data = []
      my_file = open(self.name, 'r')
      for line in my_file:
          elements = line.split (',')
      if elements[0]!='Date':
        data.append(elements)
        #print('Dati nel file: "{}"'.format(get_data()
        my_file.close()
        return data
CSVFile("shampoo_sales.csv")
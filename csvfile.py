class CSVFile():
  def __init__ (self, name):
    self.name = name
    print('Name: {}'.format(self.name))
    if not isinstance (name, str):
      raise Exception ('Errore: Il nome del file non é una stringa, non "{}" '.format(type(name)))
  def get_data(self, start=None, end=None):
    data = []
#provo ad aprire il file. in caso contrario, averto del'errore
#poi devo abortire. Questo e' un errore "un-recoverable", ovvero non posso proseguire con la lettura dei dati se non riesco ad aprire il file
    try:
      my_file = open(self.name, 'r')
    except Exception as e:
      print('Non posso aprire "my_file"')
      print('Non posso aprire un file non esistente'.format(e))
#stampo l'errore
    #return None
#se lo riesco ad aprire, lo leggo linea per linea
#se ho end, controllo che sia un intero
    for line in my_file:
         elements = line.split (',')
         elements[-1] = elements[-1].strip()
         if elements[0]!='Date':
             data.append(elements)
         if start is not None and end is not None:
           if start > end:
             raise Exception('Errore: start deve essere minore di end, invece ho avuto start ="{}", end ="{}"'.format(start,end))
           if start is None:
              start = 0
           if end is None:
              end = len (data)
           if start is not None:
            if not isinstance (start,int):
              raise Exception('Errore: il parametro "start" deve essere un intero, non "{}"'.format(type(start)))
          #se ho end, controllo che sia un intero
           if end is not None:
            if not isinstance(end, int):
              raise Exception('Errore: il parametro "end" deve essere un numero intero, non "{}"'.format(type(end)))
    my_file.close()
    return data[start:end]
my_file = CSVFile("shampoo_sales.csv")
print('Dati nel file: {}'.format(my_file.get_data()))



class NumericalCSVFile(CSVFile):
  def __init__ (self, name):
     self.name = name
     print('Name: {}'.format(self.name))
  def get_data(self):
      data = super().get_data()
      values = []
      for my_list in data:
            for item in my_list[1:]:
              try:
                item = float(item)
                values.append(item)
              except:
                print('Non posso convertire: {}'.format(item))
           
      return values
#my_filesecond = NumericalCSVFile("shampoo_sales.csv")
#print('Dati "{}":'.format(my_filesecond.get_data()))

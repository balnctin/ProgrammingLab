class ExamException(Exception):
  pass

class Diff():
  def __init__(self, ratio=1):
    self.ratio = ratio
    #Controlli
    if not isinstance(self.ratio, int) and not isinstance(self.ratio, float):
      raise ExamException('TypeError, il ratio in input non è int o float')
    if self.ratio <= 0:
      raise ExamException('Error, il ratio in input è un valore negativo')


  def compute(self, lista):
    #Controlli
    if not isinstance(lista, list):
      raise ExamException('Error, l\'input non è una lista')

    if len(lista)<=1:
      raise ExamException('Error, la lista è vuota')

    for el in lista:
      if not isinstance(el, int) and not isinstance(el, float):
        raise ExamException('TypeError, uno o più elementi della lista non sono int o float')
    

    n_list=[]
    for i in range (len(lista)-1):
      diff = lista[i+1]-lista[i]
      n_list.append(diff/self.ratio)
    return n_list
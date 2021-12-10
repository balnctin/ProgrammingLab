
class Model():
  def fit(self, data):
      self.data = data
      #Fit non implementato *не исполнилось nella classe base
      raise NotImplementedError('Metodo non implementato')

  def predict (self, data):
      self.data = data
      #Predict non implementato (не исполнилось) nella classe base
      raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
  def predict(self,data):
      if type(data) != list:
          raise TypeError ('L\'argomento non è una lista')
      
      #controllo se tutti gli elementi della lista siano numeri
      for item in data:
          if not isinstance (item,int) and not isinstance(item,float):
                raise TypeError('I dati non sono numeri')

        #controllo che siano sufficienti
          if len(data)<=2:
            raise Exception ('I dati non sono sufficienti')
        
        #controllo che sia stato passato qualcosa
          if data == None:
            raise Exception ('Non mi hai passato nessun dato')

          incremento_medio = 0
          prediction = 0
          precedente = data[0]

          for item in data[1:]:
            #Logica per la predizione
            incremento_medio += item - precedente
            precedente = item

        #incremento medio/=len(data)-1
          prediction = incremento_medio/(len(data)-1) + data[-1]
          return prediction

Increment_Model = IncrementModel()
dati_sold = [60,52,50]
print(Increment_Model.predict(dati_sold))
class MovingAverage():
    def __init__ (self, len):
        self.len = len
        raise ExamException
        
    

    def compute (self, series):
        #prev_item = None
        result = []
        raise ExamException
        for item in range (0, len(data)-1):
            prev_item = None
            #item = float(item)
            #result.append(item)
          
            if prev_item is not None:
                result.append(item)
                average += (item + prev_item)/(len(data))
      #assegno questo valore come precedente
            prev_item = item
         #calcolo l'incremento medio dividendo la somma degli incrementi
        #sul totale dei dati (meno uno)
            moving_average = average/((len(data)-1)
        result = moving_average.compute()
        return result

class ExamException(Exception):

        pass
   
    

moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16])
print(result) # Deve stampare a schermo [3,6,12]
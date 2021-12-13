
class Model():
  def fit(self, data):
      pass

  def predict (self, data):
      pass

class IncrementModel(Model):
  def __str__(self):
        return 'IncrementModel'
  def compute_avg_increment(self,data):
      #variabile di supporto per il valore precedente
        prev_item = None
      
      #preparo una variabile di supporto per calcolare l'incremento medio
        increments = 0

      #processo i mesi in input su cui fare la predizione
        for item in data:
        #Calcolo l'incremento ma se non sono al primo giro, ovvero se non è definito il "prev_item"
            if prev_item is not None:
              increments += item - prev_item

          #assegno questo valore come precedente
            prev_item = item

        #calcolo l'incremento medio dividendo la somma degli incrementi
        #sul totale dei dati (meno uno)
        avg_increment = increments/(len(data)-1)
        return avg_increment
  def predict (self, predict_data):
      #calcolo l'incremento medio sui dati della predict
      avg_increment = self.compute_avg_increment(predict_data)
      #torno la predizione (incremento medio sommato all'ultimo valore)
      return predict_data[-1] + avg_increment

class FitIncrementModel(IncrementModel):
    def __str__(self):
        return 'FitIncrementModel'

    def fit (self, fit_data):
        # Calcolo l'incremento medio sui dati di fit
        self.global_avg_increment = self.compute_avg_increment(fit_data)

    def predict(self, predict_data):
        #chiamo la predict della classe genitore "IncrementModel"
        parent_prediction = super().predict(predict_data)
      
      #sottraggo l'ultimo valore alla predizione del genitore
      #da aver l'incremento originale
        parent_predict_increment = parent_prediction - predict_data[-1]

        #ora medio l'incremento del fit con quello della predict
        prediction_increment = (self.global_avg_increment + parent_predict_increment)/2 

        #e lo ri-sommo all'ultimo elemento
        prediction = predict_data[-1]+prediction_increment
        
        return prediction

#corpo del programma
#mini-dataset di test
test_fit_data = [8,19,31,41]
test_predict_data = [50,52,60]

#test rapido su IncrementModel (non unittest in questo caso)
increment_model = IncrementModel()
prediction = increment_model.predict(test_predict_data)
if not prediction == 65:
    raise Exception ('IncrementModel sul dataset di test non mi torna 65 ma "{}"'.format(prediction))
else:
    print ('IncrementModel test passed!')

#Test rapido su FitIncrementModel (sempre non unittest in questo caso)
fit_increment_model = FitIncrementModel()
fit_increment_model.fit(test_fit_data)
prediction = increment_model.predict(test_predict_data)
if not prediction == 65.0:
    raise Exception ('FitIncrementModel sul dataset di test non mi torna 68 ma "{}"'.format(prediction))
else:
    print ('FitIncrementModel test passed')

#Linea vuota
print ('')


#I dati delle mie vendite di shampoo. In questo caso le sto direttamente scrivendo nel codice.
#ma nella realta avrei usato CSVFile e caricato i dati nel file.
#Ma così evito di avere troppe cose du cui lavorando assieme
#e visto che i dati sono piccoli, posso scriverli ed è comodo (se avevo migliaia di valori forse era meglio di no)
shampoo_sales  = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

#definisco quanti medi usare per la valutazione
#che verranno sottratto al dataset nel caso del fit
eval_months = 12
cutoff_month = len(shampoo_sales) - eval_months

#istanzio nuovo modello senza fit
increment_model = IncrementModel()

#istanzio nuovo modello con fit
fit_increment_model = FitIncrementModel()
#fitto sui dati al mese di cutoff_month
fit_increment_model.fit(shampoo_sales[0:cutoff_month])

#metto entrambi i modelli in una lista
models = [increment_model, fit_increment_model]

#switch per il plot (se messo a True bisogna chiudere la finestra del plot
#per far proseguire il programma dopo la valutazione del primo modello)
plot = False

#valuto entrambi i modelli
for model in models:
    error = 0
    print ('Evaluating model "{}"'.format(model))

    #predizioni sul dataset di "valutazione" ovvero le vendite dello shampoo dal mese di cutoff in piccoli
    predictions = []
    for i in range (eval_months):
        predict_data = shampoo_sales[cutoff_month+i-3-1:cutoff_month+i-1]
        prediction = model.predict(predict_data)
        real = shampoo_sales[cutoff_month+i]
        print('"{}"(pred) vs "{}"(real)'.format(int(prediction), int  (real)))

        #aggiungo se volessi poi plottare
        predictions.append(prediction)

        error += abs(prediction - shampoo_sales[cutoff_month+i])

    error = error / eval_months

print ('Average error:"{}"\n'.format(error))

#plotto se richiesto
if plot:
    from matplotlib import pyplot
    pyplot.plot(shampoo_sales[0:cutoff_month]+predictions,color='tab:red')
    pyplot.plot(shampoo_sales, color='tab:blue')
    pyplot.show()
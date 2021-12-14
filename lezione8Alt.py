class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    
    def compute_increments(self, data):
    #devo ricavare l'incremento medio totale
        increments = []
        for item in range(0, len(data)-1):
            one_month = data[item+1] - data[item]
            increments.append(one_month)
        
        tot_incr = sum(increments)
        #len(data)-1 perchè il primo mese non può avere qualcosa di sottratto
        avg_incr = tot_incr / (len(data)-1)

        return avg_incr

    def predict(self, data):
        avg_incr = self.compute_increments(data)
        prediction = data[-1] + avg_incr
        return prediction


lista = [50, 52, 60]

obj = IncrementModel()
prediction = obj.predict(lista)
print(prediction)
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

class FitIncrementModel(IncrementModel):
    
    def fit(self, fitdata):
        self.tot_avg_incr = super().compute_increments(fitdata)

    def predict(self, preddata):
        parent_pred = super().predict(preddata)
        #valore ultimo mese - valore penultimo mese
        parent_pred_incr = parent_pred - preddata[-1]
        new_pred_incr = (self.tot_avg_incr + parent_pred_incr) / 2
        new_pred = preddata[-1] + new_pred_incr

        return new_pred

fit_data = [266.0,145.9,183.1,119.3,180.3,168.5,231.8,224.5,192.8,122.9,336.5,194.3,149.5,210.1,273.3,191.4,287.0,226.0,303.6,289.9,421.6,264.5,342.3,339.7,440.4,315.9,439.3,401.3,437.4,575.5,407.6,682.0]
pred_data = [475.3,581.3,646.9]

obj1 = IncrementModel()
prediction = obj1.predict(pred_data)
print(prediction)

obj2 = FitIncrementModel()
obj2.fit(fit_data)
fitted_prediction = obj2.predict(pred_data)
print(fitted_prediction)
    


         

        


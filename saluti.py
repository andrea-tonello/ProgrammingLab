class CSVFile():
    
    def __init__(self,file):
        self.filename = file

        self.can_read = True
        try:
            f=open(self.filename, 'r')
            f.readline()
        except Exception as e:
            self.can_read = False
            print(f'Errore in apertura del file:\n{e}')

    def get_data(self):
        if not self.can_read:
            print('Non è stato possibile aprire il file')
            exit()
        else:
            valori=[]
            file=open(self.filename,'r')
            for line in file:
                elements = line.split(',')
                elements[-1] = elements[-1].strip()
                if elements[0] != 'Date':
                    valori.append(elements)
            file.close()
            return valori

#con questa classe voglio convertire i valori dalla colonna due in su a float (da string)
class FloatCSVFile(CSVFile):
    
    def get_data(self):
        
        float_data = []
        og_data = super().get_data()
        
        for og_row in og_data:
            float_row = []
            
            for i,element in enumerate(og_row):
                if i==0:
                    pass
                else:
                    try:
                        float_row.append(float(element))
                    except Exception as e:
                        print(f'Errore di conversione della stringa:\n{e}')
                        break
        
            float_data.append(float_row)
        
        return float_data

    
class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    
    def predict(self, data):
        self.data = data
        all_data = self.data
        
        values_per_month = []
        l = len(all_data)

        for i in range(0, l-1):
            one_month = all_data[i+1] - all_data[i]
            values_per_month.append(one_month)
        
        somma_vpm = sum(values_per_month)
        lung_vpm = len(values_per_month)
        avg_vpm = somma_vpm / lung_vpm

        pred_result = data[-1] + avg_vpm
            
        return pred_result


miei_valori = FloatCSVFile('shampoo_sales.csv')
mia_lista = miei_valori.get_data()

#mia_lista è fatta così: [[a], [b], [c]...] ma a me serve = [a, b, c...]
#altrimenti nel for di predict non posso sommare a+b+c..., perciò:
mia_lista_flat = []
for item in mia_lista:
    mia_lista_flat = mia_lista_flat + item

mio_oggetto2 = IncrementModel()
result = mio_oggetto2.predict(mia_lista_flat)
print(result)
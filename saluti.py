from matplotlib import pyplot

class CSVFile():
    def __init__(self, name, file):
        self.name = name
        self.file = file

    def write(self, line):
        my_file = open(self.file, 'a')
        my_file.write('\n'+line)
        my_file.close()

    def get_data(self):
        my_list = []
        try:
            my_file = open(self.file, 'r')
            for line in my_file:
                elem = line.rstrip().split(',')
                if elem[0] != 'Date':
                    my_list.append(elem)
            my_file.close()
            return my_list;
        except Exception as e:
            print('ERROR: Impossibile aprire file "{}"'.format(self.file))

class Model():
    def fit(self, data):
        raise NotImplementedError("Metodo non implementato")
    def predict(self, data):
        raise NotImplementedError("Metodo non implementato")        

class IncrementedModel(Model):
    def check_data(self, data):
        if len(data)<2:
            return 'Impossibile fare previsione, numero di dati insufficienti'
        else:
            return True
    #def preditct(self, data):  

class FitIncrementModel(IncrementedModel):
    def fit(self, data):
        if self.check_data(data):
            inc = 0.0
            #controllo se ci sono errori nel file come stringhe al posto di float
            for i in range(0, len(data)-1):
                inc += float(data[i+1]) - float(data[i])    
            global_avg_increment = inc/len(data)
            return global_avg_increment
        else:
            print(self.check_data(data))
    
    def predict(self, data, global_avg_increment):
        prediction = float(data[len(data)-1]) + global_avg_increment
        data.append(prediction)
        return data
        
csvobj = CSVFile('Vendite shampoo', 'shampoo_sales.csv')
my_list = csvobj.get_data()
print(my_list)
data = []
values = []
for item in my_list:
    data.append(item[1])
fitobj = FitIncrementModel()

#numero di mesi di cui voglio predire i valori
number_of_months = 12

for i in range(1, number_of_months+1):
    global_avg_increment = fitobj.fit(data)
    values = fitobj.predict(data, global_avg_increment)
    csvobj.write('prediction '+str(i)+','+str(round(values[len(values)-1], 2)))
    
pyplot.plot(data, color='tab:blue')
pyplot.plot(values, color='tab:red')
pyplot.show()
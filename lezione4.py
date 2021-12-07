class CSVFile():
    
    def __init__(self, file):
        self.file = file

    def get_data(self):
        valori=[]
        
        file=open(self.file,'r')
        
        for line in file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip('\n')

            valori.append(elements)
        
        file.close()
        return valori

valori = []
mio_oggetto = CSVFile('shampoo_sales_2.csv')
valori = mio_oggetto.get_data()
for line in valori:
    print(line)



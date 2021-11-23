class CSVFile():
    
    def __init__(self,name,file):
        self.nome = name
        self.file = file

    def get_data(self):
        valori=[]
        file=open(self.file,'r')
        for line in file:
            elements = line.split(',') 

            valori.append(elements)
        return valori

valori = []
mio_oggetto = CSVFile('Vendite', 'shampoo_sales.csv')
valori = mio_oggetto.get_data()
for line in valori:
    print(line)



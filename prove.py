class CSVFile():
    
    def __init__(self,file):
    
        try:
            f=open(file, 'r')
            f.readline()
            self.filename = file
        except Exception as e:
            print (f'Errore in apertura del file:{e}')
            exit()
            

    def get_data(self):
        valori=[]
        file=open(self.filename,'r')
        for line in file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip()
            if elements[0] != 'Date':
                valori.append(elements)
        file.close()
        return valori


lista_prova = []
obj = CSVFile(3)
lista_prova = obj.get_data()

for item in lista_prova:
    print(item)

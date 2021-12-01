class CSVFile():
    
    def __init__(self,name,file):
        self.nome = name
        self.file = file

    def get_data(self):
        valori = []
        file = open(self.file,'r')
        for line in file:
            valori.append(line)
        return valori
        file.close()
    
    def get_date_vendite(self):
        dates = []
        file = open(self.file, 'r')
        for line in file:
            elements = line.split(',')
            dates.append(elements[0])
        return dates
        file.close()

    def __str__(self):
        file = open(self.file, 'r')
        file_contents = file.read()
        header = file_contents[0:11]
        return header
        file.close()

mio_oggetto = CSVFile('Vendite', 'shampoo_sales.csv')

valori = mio_oggetto.get_data()
for line in valori:
    print(line)

dates = mio_oggetto.get_date_vendite()
for line in dates:
    print(line)

print()

header = mio_oggetto.__str__()
print(header)


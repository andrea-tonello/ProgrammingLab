class NotString(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg


class CSVFile():
    
    def __init__(self, filename):
        self.filename = filename
        try:
            if isinstance(self.filename, str): #if type(self.filename) == str:if isinstance(self.filename, str)
                pass
            else:
                raise NotString('Il nome del file non è una stringa; esso è: {}'.format(type(self.filename)))
        except NotString as e:
            print(e.error_msg)
        
            

    def get_data(self):
        valori=[]
        file=open(self.filename,'r')
        for line in file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip()

            valori.append(elements)
        file.close()
        return valori



mio_oggetto = CSVFile(6)
valori = mio_oggetto.get_data()
for line in valori:
    print(line)

#shampoo_sales_2.csv
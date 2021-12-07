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
                    float_row.append(element)
                else:
                    try:
                        float_row.append(float(element))
                    except Exception as e:
                        print(f'Errore di conversione della stringa:\n{e}')
                        break
        
            if len(float_row) == len(og_row):  #la consegna mi chiede di skippare le righe che danno errori
                float_data.append(float_row)
            else:                              #con else, invece di skipparla, la riporto con la dicitura che segue
                float_data.append('// Stringa non convertibile //')
        
        return float_data


mio_oggetto = CSVFile('shampoo_sales_3.csv')
print(f'LISTA ORIGINALE: "{mio_oggetto.filename}"\n')
lista1 = mio_oggetto.get_data()
for line in lista1:
    print(line)

print('\n')

mio_oggetto2 = FloatCSVFile('shampoo_sales_3.csv')
print(f'LISTA CONVERTITA: "{mio_oggetto2.filename}"\n')
lista2 = mio_oggetto2.get_data()
for line in lista2:
    print(line)


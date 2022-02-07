from datetime import datetime 

class NotString(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg


class CSVFile():
    
    def __init__(self, filename):
        self.filename = filename
        
        try:
            if not isinstance(self.filename, str): #if type(self.filename) == str:
                raise NotString('Il nome del file non è una stringa!')
        except NotString as e:
            print(e.error_msg)
            print('Il file è stato digitato come: {}'.format(type(self.filename)))
            print()
            print('File selezionato:\n"{}"'.format(self.filename))
            exit() #opzionale
        
    
    def file_name(self):
        return 'File selezionato:\n"{}"'.format(self.filename)
    
    
    def get_data(self, start=None, end=None):
        valori=[]
        
        file=open(self.filename,'r')
        all_lines = file.readlines()

#con enumerate conto le righe e con lo slicing levo le righe che non mi servono   
        for i,line in enumerate(all_lines[start:end]):      
            
            elements = line.split(',')
            elements[-1] = elements[-1].strip('\n')

#controllo che il formato degli elementi della prima colonna sia gg-mm-aaaa
            try: 
                if datetime.strptime(elements[0],'%d-%m-%Y'):
                    valori.append(elements)
            except ValueError:
                print('Errore a riga {}\n'.format(i))           
                valori.append('// Controllare la data inserita //')

#verifico che nelle colonne successive ci siano solo numeri
        
        file.close()
        return valori



mio_oggetto = CSVFile('shampoo_sales_3.csv')

try:
    valori = mio_oggetto.get_data(1,8)

except FileNotFoundError:               #FileNotFoundError è built-in
    print('Il file non esiste o non è stata specificata la sua estensione')

except UnicodeDecodeError as e:         #UnicodeDecodeError è built-in
    print('Assicurarsi che l\'estensione del file sia testuale')
    print('Specifiche errore:\n{}'.format(e))

else: #stampo i valori se sono passati il check dell'__init__ e i due check qua sopra
    for line in valori:
        print(line)
finally:
    print()
    print(mio_oggetto.file_name())

#'shampoo_sales_2.csv'
#'saluti.txt'
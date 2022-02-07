from datetime import datetime 

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    
    def __init__(self,name):
        self.file = name

    def get_data(self):
        
        valori = []
        f=open(self.file,'r')
        lines = f.readlines()
        
        for line in lines:
            minilist = []  # = item della lista annidata
            elements = line.split(',')
            elements[-1] = elements[-1].strip()
            try: minilist.append(str(elements[0]))
            except: pass
            try: minilist.append(elements[1])
            except: pass
            
            valori.append(minilist)
        
#controllo formato di prima e seconda riga
        for item in valori:
            try: datetime.strptime(item[0],'%Y-%m')
            except: valori.remove(item)
        for item in valori:
            try: item[1] = int(item[1])
            except: valori.remove(item)

        return valori


#ricorda: devo passare time_series già sanitizzata altrimenti è uno scazzo
def compute_avg_monthly_difference(time_series=None, first_year=None, last_year=None):

#check esistenza di time_series
    if time_series == None: raise ExamException('Nessuna lista in input!')
#type check di time_series
    if not isinstance(time_series, list): raise ExamException('time series deve essere una lista!')
#controllo che time_series non sia vuota
    if len(time_series) == 0: raise ExamException('time_series non contiene alcun dato')

#check esistenza estremi
    if first_year == None: raise ExamException('Nessun estremo inferiore in input!')
    if last_year == None: raise ExamException('Nessun estremo superiore in input!')
#check formato estremi
    #per qualche motivo usare type(first_year or last_year) causa problemi
    if type(first_year) != str: raise ExamException('Il formato degli estremi deve essere str!')
    if type(last_year) != str: raise ExamException('Il formato degli estremi deve essere str!')

#check valore intrinseco degli estremi  !!! RIVEDERE !!!
    try: int(first_year)
    except Exception as e: raise ExamException(f'Errore: {e}')
    try: int(last_year)
    except: raise ExamException('Il valore degli estremi deve essere un anno, numero intero')
#check ordine estremi
    if int(first_year) > int(last_year): raise ExamException('first_year non puo essere maggiore di last_year')
#check uguaglianza estremi
    if int(first_year) > int(last_year): raise ExamException('first_year e last_year non possono essere uguali')

#controllo che gli estremi siano in time_series
    check_first = False
    check_last = False
    
    x = True
    while x:
        for minilist in time_series:
            if first_year in minilist[0]:
                check_first = True
                x = False
        x = False

    y = True
    while y:
        for minilist in time_series:
            if last_year in minilist[0]:
                check_last = True
                y = False
        y = False

    if check_first == False: raise ExamException('Controllare l\'estremo inferiore')
    if check_last == False: raise ExamException('Controllare l\'estremo superiore')
    return check_first, check_last






time_series_file = CSVTimeSeriesFile('data.csv')
time_series = time_series_file.get_data()
#print(time_series)

print(compute_avg_monthly_difference (time_series, '1949', '1960'))
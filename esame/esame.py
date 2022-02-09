from datetime import datetime 

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
#check input nullo o non valido
    def __init__(self, name=None):
        if name == None: raise ExamException('Inserire un file')
        if type(name) is not str: raise ExamException('Ricontrollare file in input')
        self.file = name

    def get_data(self):
#check esistenza del file
        try:
            file = open(self.file, 'r')
            check_file1 = True
        except:
            check_file1 = False
        if check_file1 == False: raise ExamException ('Impossibile aprire il file')
#check leggibilità del file
        try:
            file.readlines()
            check_file2 = True
        except:
            check_file2 = False    
        if check_file2 == False: raise ExamException ('Impossibile leggere il file')
        
        valori = []
        file=open(self.file,'r')
        lines = file.readlines()
        
        for line in lines:
            minilist = []  # = item della lista annidata
            elements = 0
            if ',' in line:
                elements = line.split(',')
                elements[-1] = elements[-1].strip()
                try: minilist.append(elements[0])
                except: pass
                try: minilist.append(elements[1])
                except: pass
            else: pass
            
            valori.append(minilist)
            
            for item in valori:
                try: datetime.strptime(item[0],'%Y-%m')
                except: valori.remove(item)
            for item in valori:
                try: 
                    item[1] = int(item[1])
                    if item[1] < 0:
                        valori.remove(item)
                except: valori.remove(item)
                if item[1] == None:
                    valori.remove(item)

        file.close()
        return valori


def find_first(time_series):
    i=0
    res = 0
    while i<12:
        try:
            elem = time_series[i][0].split('-')
            res = elem[0]
            return int(res)
            break
        except: pass
        i += 1
    
        
#ricorda: devo passare time_series già sanitizzata altrimenti è uno scazzo
def compute_avg_monthly_difference(time_series=None, first_year=None, last_year=None):

#-------------[CONTROLLO TIME_SERIES]-------------
#check esistenza di time_series
    if time_series == None: raise ExamException('Nessuna lista in input!')
#type check di time_series
    if not isinstance(time_series, list): raise ExamException('time series deve essere una lista!')
#controllo che time_series non sia vuota
    if len(time_series) == 0: raise ExamException('time_series non contiene alcun dato')
#-----------------------------------------------------------

#-------------[CONTROLLO FIRST_YEAR, LAST_YEAR]-------------
#check esistenza estremi
    if first_year == None: raise ExamException('Nessun estremo inferiore in input!')
    if last_year == None: raise ExamException('Nessun estremo superiore in input!')

#check formato estremi
    #per qualche motivo usare type(first_year or last_year) causa problemi
    if type(first_year) != str: raise ExamException('Il formato degli estremi deve essere str!')
    if type(last_year) != str: raise ExamException('Il formato degli estremi deve essere str!')

#check valore intrinseco degli estremi
    try: 
        int(first_year)
        check_int1 = True
    except: 
        check_int1 = False
    if check_int1 == False: raise ExamException('Il valore degli estremi deve essere un anno, numero intero')
    try: 
        int(last_year)
        check_int2 = True
    except:
        check_int2 = False
    if check_int2 == False: raise ExamException('Il valore degli estremi deve essere un anno, numero intero')

#check ordine estremi
    if int(first_year) > int(last_year): raise ExamException('first_year non puo essere maggiore di last_year')
#check uguaglianza estremi
    if int(first_year) == int(last_year): raise ExamException('first_year e last_year non possono essere uguali')

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
#-----------------------------------------------------------
#val_per_month[i] conterrà tutti i valori (numero di passeggeri) dell'i-esimo mese
    first = int(first_year)
    last = int(last_year)
    total_years = last - first + 1
        
    filled_time_series = []
    for i in range(total_years):
        filled_time_series.append([])
        for j in range (0,12):
            filled_time_series[i].append(['-1',-1])

    time_series2 = []

    for i in range (first, last+1):
        tmplist = []
        for item in time_series:
            date = item[0].split('-')
            if str(i) == date[0]:
                tmplist.append(item)
        time_series2.append(tmplist)

    for i,lista in enumerate(time_series2):
        for element in lista:
            date = element[0].split('-')
            month = date[1]
            monthint = int(month)
        
            for j in range(12):
                if j == monthint-1:
                    filled_time_series[i][j] = element

    flat_time_series = [item for sublist in filled_time_series for item in sublist]
    
    val_per_month = []
    for i in range(0,12):
        val_per_month.append([])

    #devo cercare il primo anno presente in time_series
    true_first = (find_first(flat_time_series))
    
    month_index = (first - true_first) * 12
    for i in range(0, 12):
        sum = 0
        for j in range(0, total_years):
            val_per_month[i].append(flat_time_series[month_index+sum][1])
            sum += 12
        month_index += 1
    
    #for month in val_per_month:
    #    print(month)
    #print()
#tolgo i valori nulli-------------------------------------------------
    val_per_month = [[value for value in month if value > -1] for month in val_per_month]
    
    #for month in val_per_month:
    #    print(month)
    #print()
#calcolo l'incremento------------------------------------------------
    results = []
    for month in val_per_month:
        if len(month) <= 1:
            results.append(0)
        else:
            res = 0
            i = 1
            while i<len(month):
                res = res + (month[i]-month[i-1])
                i += 1
            #print(res)
            results.append(res / (len(month)-1))

    return results
            
    
time_series_file = CSVTimeSeriesFile('data(copy2).csv')
time_series = time_series_file.get_data()
#print(time_series)

print(compute_avg_monthly_difference (time_series, '1950', '1955'))
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

def compute_avg_monthly_difference(time_series, first_year, last_year):
    #final_values = []
#check formato estremi
#check ordine estremi
    if int(first_year) >= int(last_year): raise ExamException('Controllare la cronologia degli estremi')
# existence checking sugli estremi 
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

print(compute_avg_monthly_difference(time_series, '1965', '1945'))
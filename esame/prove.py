from datetime import datetime 

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    
    def __init__(self,name):
        self.file = name

    def get_data(self):
        try:
            file = open(self.file, 'r')
            check_file1 = True
        except Exception:
            check_file1 = False
            
        if check_file1 == False: raise ExamException ('Impossibile aprire il file')

        try:
            file.readlines()
            check_file2 = True
        except Exception:
            check_file2 = False
            
        if check_file2 == False: raise ExamException ('Impossibile leggere il file')

        file = open(self.file, 'r')
        valori = []
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



time_series_file = CSVTimeSeriesFile('data(copy).csv')
time_series = time_series_file.get_data()
print(time_series)
print()

total_years = 1951-1949+1
filled_time_series = []
for i in range(total_years):
    filled_time_series.append([])
    for j in range (0,12):
        filled_time_series[i].append(['-1',1])

print(filled_time_series)
print()

'''#for i in range(total_years):
    
for item in time_series:
    date = item[0]
    y_m = date.split('-')
    y_m_int = int(y_m[1])
    for i in range (total_years):
        filled_time_series.insert((y_m_int-1), [y_m[0]+'-'+y_m[1],item[1]])
    
print(filled_time_series)'''



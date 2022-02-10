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

        print(valori)
#controllo duplicati
        duplicato = any(valori.count(item) > 1 for item in valori)
        if duplicato == True:
            raise ExamException('Ci sono dei valori duplicati!')

#controllo ordine: anni
        year_sort = []
        for item in valori:
            date = item[0].split('-')
            year_sort.append(int(date[0]))

        order_check1 = True
        if (year_sort != sorted(year_sort)):
            order_check1 = False

        if order_check1 == False:
            raise ExamException('Anni non in ordine!')

#controllo ordine: mesi per ogni anno
        #voglio il numero di anni totali
        year_sort = list( dict.fromkeys(year_sort) )
        tot_years = len(year_sort)
        
        first = year_sort[0]
        last = year_sort[-1]
        valori_regrouped = []
        
        for i in range(first, last+1):
            tmplist = []
            for item in valori:
                date = item[0].split('-')
                if str(i) == date[0]:
                    tmplist.append(date)
            valori_regrouped.append(tmplist)

        print()
            
        #ora che valori_regrouped è organizzata per anno, faccio il check su ogni mese per ogni anno
        order_check2 = True
        for item in valori_regrouped:
            tmplist = []
            for i in item:
                tmplist.append(int(i[1]))
            if (tmplist != sorted(tmplist)):
                order_check2 = False

        if order_check2 == False:
            raise ExamException('Mesi non in ordine!')
        
        print()
        #print(valori_regrouped)
        
        file.close()
        return valori


time_series_file = CSVTimeSeriesFile(name = None)
time_series_file = CSVTimeSeriesFile('data(copy).csv')
time_series = time_series_file.get_data()
#print(time_series)
import os
#mi serve per os.path.isfile()

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    #check input nullo o non valido
    def __init__(self, name=None):
        if name == None: raise ExamException('Inserire un file')
        if type(name) is not str: raise ExamException('Ricontrollare file in input')
        self.name = name

    def get_data(self):
        #devo controllare prima che non fosse None e che non fosse una lista, altrimenti non reisco a verificare la condizione sottostante perchè isfile() non accetta come parametro None o liste
        if self.name is not None and not isinstance(self.name, list):

            #controllo se il file esiste e/o se quello che viene passato come parametro nella __init__ è un file
            if os.path.isfile(self.name):
                my_list = []
                years_and_months = []
                last_date = [0, 0]
                current_line = 0
                #try:
                my_file = open(self.name, 'r')
                #controllo se il file è vuoto
                if os.stat(self.name).st_size == 0:
                    raise ExamException('ERROR: file vuoto')
                else:
                    for line in my_file:
                        current_line += 1
                        #controllo se la riga non è vuota e se contiene la virgola
                        if line != '\n' and ',' in line:
                            elem = line.rstrip().split(',')
                            if elem[0] != 'date':
                                
                                elem[0] = str(elem[0])
                                #controllo se è presente il trattino
                                if '-' not in elem[0]:
                                    print('ERROR: anomalia a riga {}'.format(current_line))
                                #controllo se quella data è già presente
                                elif elem[0].rstrip().split('-') in years_and_months:
                                    raise ExamException('ERROR: nel file è presente un duplicato di {}'.format(elem[0]))
                                else:
                                    years_and_months.append(elem[0].rstrip().split('-'))
                                    #ogni elemento di years_and_months contiene una lista del tipo ['1953', '05']

                                    #mi salvo la data corrente per poi vedere se il file è ordinato
                                    current_date = elem[0].rstrip().split('-')
                                    
                                    try:
                                        current_date[0] = int(current_date[0])
                                        current_date[1] = int(current_date[1])
                                        converted_in_int = True
                                    except ValueError:
                                        converted_in_int = False
                                        print('ERROR: impossibile convertire {} in int'.format(current_date))
                                    if converted_in_int:
                                        #controllo se c'è un timestamp non in ordine
                                        if current_date[0] <= last_date[0] and current_date[1] <= last_date[1]:
                                            raise ExamException('ERROR: elemento "{}" non ordinato in modo crescente'.format(elem[0]))
                                            
                                        #controllo che il mese sia compreso tra 1 e 12
                                        elif int(current_date[1])<=0 or int(current_date[1])>12:
                                            raise ExamException('ERROR: elemento "{}" non rispetta i canoni'.format(elem[0]))
                                        else:
                                            last_date[0] = int(current_date[0])
                                            last_date[1] = int(current_date[1])
                                        
                                        
                                        #controllo se ci sono pezzi di codice in più dopo il valore dei passeggeri
                                        #aus = elem[1].rstrip().split(' ')
                                        #if len(aus) > 1:
                                            #elem[1] = aus[0]

                                        try:
                                            #converto le migliaia di passeggeri in intero
                                            elem[1] = int(elem[1])
                                            
                                            #controllo se ho un valore nullo o negativo
                                            if elem[1] <= 0:
                                                print('ERROR: impossibile computare "{}"'.format(elem[1]))
                                            else:
                                                my_list.append(elem)
                                        except Exception as e:
                                            print('ERROR: impossibile convertire valore passeggeri "{}" della riga {} in int'.format(elem[1], current_line))
                                    
                    return my_list;
                my_file.close()                    
                #except Exception as e:
                    #print('ERROR: impossibile computare il file "{}"'.format(self.name))
            else:
                raise ExamException('ERROR: file non leggibile o inesistente')
        else:
            raise ExamException('ERROR: il file da leggere è None o è una lista')

### FUNCTIONS ###

#funzione per verificare se first_year e/o last_year è presente nel file
def year_in_file(time_series, year):  
    list_of_years = []
    for item in time_series:
        elem = str(item[0]) #prendo anno e mese insieme
        year_and_month = elem.rstrip().split('-')
        #in year_and_month viene messa una lista del tipo ['1953', '05']
        list_of_years.append(int(year_and_month[0]))
    if (year in list_of_years):
        return True
    else:
        return False
    
#funzione per verificare se un determinato parametro può essere accettato
def parameter_ok(parameter):    
    if parameter is not None and type(parameter) == str:
        return True
    else:
        return False

#funzione per verificare che time_series sia una lista e che non sia None
def time_series_ok(time_series):
    if time_series is not None and isinstance(time_series, list):
        for item in time_series:
            #controllo se l'elemento non è None e se c'è la virgola
            if item is not None and ',' in str(item):
                return True 
            else:
                return False
    else:
        return False
    
def compute_avg_monthly_difference(time_series, first_year, last_year):
    months = []
    passengers = []
    converted_in_int = True
    if parameter_ok(first_year) and parameter_ok(last_year):
        try:
            first_year = int(first_year)
            last_year = int(last_year)
        except ValueError:
            converted_in_int = False
            print('ERROR: impossibile convertire first_year e/o last_year in int')
        if converted_in_int:
            #controllo che time_series sia accettabile
            if time_series_ok(time_series):
                #controllo che first_year e last_year siano compresi nel file
                if year_in_file(time_series, first_year) and year_in_file(time_series, last_year):

                    #controllo se first_year è uguale da last_year
                    if first_year == last_year:
                        raise ExamException('ERROR: impossibile calcolare variazione, first_year e last_year sono uguali')
                    else:
                        #controllo se first_year è maggiore di last_year, nel caso li inverto
                        if first_year > last_year:
                            first_year, last_year = last_year, first_year
                        
                        for item in time_series:
                            #prendo anno e mese insieme
                            elem = str(item[0])
                            year_and_month = elem.rstrip().split('-')
                            #in year_and_month viene messa una lista del tipo ['1953', '05']
                            if int(year_and_month[0]) >= first_year and int(year_and_month[0])<= last_year:
                                #creo due liste, una per i mesi ed una per i corrispettivi valori dei passeggeri
                                months.append(int(year_and_month[1]))
                                passengers.append(int(item[1]))

                        #inizializzo la lista delle variazioni medie con ogni elemento = 0, in modo da poter utilizzare successivamente il +=
                        avg_variation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                        #faccio la differenza che corrisponde agli anni su cui devo fare i calcoli -1
                        diff = last_year - first_year

                        #mi serve per contare di quanti e di quali mesi ho la misurazione
                        freq_of_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                        for i in range (0,12):
                            #conto quante misurazioni ho per quel mese
                            freq_of_month[i] += months.count(i+1)
                            #prev_value
                            previous_value = 0
                            for j in range(0, len(months)):
                                if i+1 == months[j]:
                                    #se è la prima volta che "incontro" quel mese mi salvo il valore dei passeggeri
                                    if previous_value == 0:
                                        previous_value = passengers[j]
                                    #altrimenti faccio il valore attuale dei passeggeri per quel mese meno il valore precedente (sempre di quel mese) e poi aggiorno previous_value
                                    else:
                                        avg_variation[i] += passengers[j] - previous_value
                                        previous_value = passengers[j]
                            #intervallo di due anni e meno di due misurazioni
                            if diff == 1 and freq_of_month[i] < 2:
                                avg_variation[i] = 0
                            #intervallo di più di due anni e meno di due misurazioni
                            elif diff > 1 and freq_of_month[i] < 2:
                                avg_variation[i] = 0
                            #intervallo di più di due anni e ho almeno due misurazioni, ma comunque ne manca almeno una
                            elif diff > 1 and freq_of_month[i] <= diff:
                                avg_variation[i] /= freq_of_month[i]-1
                            #intervallo di n anni e ho n misurazioni
                            else:
                                avg_variation[i] /= diff

                        return avg_variation
                else:
                    raise ExamException('ERROR: first_year e/o last_year non presente nel file')
            else:
                raise ExamException('ERROR: time_series non computabile')
        else:
            print('ERROR: impossibile procedere senza covertire in intero first_year e/o last_year')
    else:
        raise ExamException('ERROR: valore di first_year e/o di last_year non computabile')

time_series_file = CSVTimeSeriesFile('data(copy).csv')
time_series = time_series_file.get_data()
#print(time_series)

print(compute_avg_monthly_difference (time_series, '1949', '1951'))
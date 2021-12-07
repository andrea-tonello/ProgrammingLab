#myfile = open('shampoo_sales.csv', 'r')
#print(myfile.read()[0:50])
#myfile.close()

# Apro il file
#my_file = open('shampoo_sales.csv', 'r')
# Leggo il contenuto
#my_file_contents = my_file.read()
# Stampo a schermo i primi 50 caratteri + qualcos'altro
#if len(my_file_contents) > 50:
 #print(my_file_contents[0:50] + ' cacca')
#else:
 #print(my_file_contents)
# Chiudo il file
#my_file.close()


#my_file = open('shampoo_sales.csv', 'r')
#print(my_file.readline())
#print(my_file.readline())
#my_file.close()

#myfile2=open('saluti.txt', 'w')
#myfile2.write('Ciao mondo')
#myfile2.close()

#myfile3 = open('saluti.txt', 'r')
#print(myfile3.read())
#myfile3.close()


def somma():
    valori=[]
    risultato=0
    myfile=open('shampoo_sales.csv', 'r')
    for line in myfile:
        elements = line.split(',') #splitto ogni linea dove c'è una virgola, questo crea una lista composta da due elementi [0,1]
        if elements[0] != 'Date' and elements[1] != 'Sales':
            lista_delle_date=elements[0]
            lista_di_valori=elements[1]
            
            valori.append(lista_delle_date)
            valori.append(float(lista_di_valori))
       
    
    '''for numeri in valori:
        risultato=risultato + numeri
    return risultato'''
    return valori
    
    myfile.close()

valori = somma()

for item in valori:
    print(item)
    



           
       
        
        
        

def stampa(lista):
    for item in lista:
        print(item)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def statistiche(lista):
    final_list = []
    for item in lista:
        if type(item)==int:
            continue
        else:
            print("La lista inserita non è composta da soli interi")
            exit()

    somma = 0
    for item in lista:
        somma = somma+item
    final_list.append(somma)

    media = somma/len(lista)
    final_list.append(media)

    minimo = min(lista)
    final_list.append(minimo)

    massimo = max(lista)
    final_list.append(massimo)

    return final_list
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def somma_vettoriale(lista, lista2):
    for item in lista or lista2:
        if type(item)!=int:
            print("Le liste accettano solo valori interi")
            return final_list
            exit()
    if len(lista)==len(lista2):
        zipped_lists = zip(lista, lista2)
        final_list = [i + j for (i,j) in zipped_lists]
    else:
        print("Le liste non sono della stessa lunghezza")
    
    return final_list   
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   

my_list = [6,4,3,1]
my_list2 = [7,8,9,0]

stampa(my_list)
print("Le statistiche base della lista sono: {}".format(statistiche(my_list)))
print("La somma vettoriale è {}".format(somma_vettoriale(my_list,my_list2)))

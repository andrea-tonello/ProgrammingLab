def stampa(lista):
    for item in lista:
        print(item)

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

def somma_vettoriale(lista, lista2):
    for item in lista and lista2:
        if type(item)==int:
            continue
        else:
            print("La liste inserite non sono composte da soli interi")
            exit()


my_list = [6,4,3,1]
my_list2 = [7,8,9,0]

stampa(my_list)
print("Le statistiche base della lista sono: {}".format(statistiche(my_list)))

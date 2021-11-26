def somma_vettoriale(lista, lista2):
    final_list = []
    for item in lista or lista2:
        if type(item)!=int:
            print("Le liste accettano solo valori interi")
            return final_list
            exit()
    if len(lista)==len(lista2):
        final_list = sum(lista) + sum(lista2)
    else:
        print("Le liste non sono della stessa lunghezza")
    
    return final_list
    

my_list = [6,4,3,1.4]
my_list2 = [7,8,9,0]
print("La somma vettoriale è {}".format(somma_vettoriale(my_list,my_list2)))
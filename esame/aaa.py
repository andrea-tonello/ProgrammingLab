lista = [[2,None,2,0],[0,None,0,2],[None,2,2,2],[None,0,0,0]]
print (lista)
lista = [[value for value in i if value != None] for i in lista]
print (lista)

'''for item in lista: 
    if item <= 0:
        lista.remove(item)'''


#matrix = [[j for j in range(5)] for i in range(5)]
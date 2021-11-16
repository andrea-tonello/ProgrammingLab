def somma(lista):
    risultato=0
    for numero in lista:
        risultato = risultato+numero
    return risultato

lista = [1,2,3,4]
print('La somma è: {}'.format(somma(lista)))
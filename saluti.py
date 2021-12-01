x = '6.0'

try:
    x = int(x)
    print('Posso convertire')
    print(x)
except ValueError as cac:
    print('Non posso convertire, porto x a 0')
    x = 0
    print(x)
    print('Errore di Valore: {}'.format(cac))
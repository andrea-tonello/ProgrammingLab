class ExamException(Exception):
    pass

class ExamException(Exception):
    pass

def func(lista = None, altro = None):
    if lista == None:
        raise ExamException('lista nulla')
    return lista[0]

print(func())


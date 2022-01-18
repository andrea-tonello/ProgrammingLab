class ExamException(Exception):
    pass

class Diff():

    def __init__(self, ratio = 1):

        if ratio == None:
            raise ExamException('Input = None!')

        if not isinstance(ratio, (int, float)):
            raise ExamException('Ratio deve essere un numero')

        if ratio < 1:
            raise ExamException('Ratio deve essere >= 1')

        #check passati
        self.ratio = ratio

    def compute(self, lista = None):

        if lista == None:
            raise ExamException('Nessun parametro in input')

        if type(lista) is not list:
            raise ExamException('L\'input deve essere una lista!')

        if len(lista) == 0:
            raise ExamException('La lista è vuota')

        if len(lista) == 1:
            raise ExamException('La lista deve avere almeno due elementi')

        if not all(isinstance(i, (int, float)) for i in lista):
            raise ExamException('I valori della lista devono essere numerici')

        final_list = []

        i=0
        while i < len(lista)-1:
            final_list.append((lista[i+1] - lista[i]) / self.ratio)
            i += 1

        return final_list

diff = Diff()
res = diff.compute([2,4])
print(res)




        
class ExamException(Exception):
    pass

class MovingAverage():
    
    def __init__(self, moving_interval = None):

        if moving_interval == None:
            raise ExamException('Non è stato passato nulla in input')
        
        if type(moving_interval) is not int:
            raise ExamException('L\'intervallo deve di tipo int!')

        if moving_interval <= 0:
            raise ExamException('L\'intervallo deve essere un intero positivo!')

        self.interval = moving_interval
        
    def compute(self, value_list = None):

        if value_list == None:
            raise ExamException('Necessario passare una lista come parametro!')

        if type(value_list) is not list:
            raise ExamException('Il parametro deve essere una lista!')

        if self.interval > len(value_list):
            raise ExamException(f'L\'intervallo deve essere <= alla lunghezza della lista, invece è lungo {self.interval}')

        if not all(isinstance(i, (int, float)) for i in value_list):
            raise ExamException('I valori della lista possono solo essere int o float!')
        
        final_list = []
        
        i=0
        while i <= len(value_list) - self.interval:
            single_list = value_list[i:i+self.interval]
            average = sum(single_list) / len(single_list)

            final_list.append(average)
            i += 1
        
        return final_list





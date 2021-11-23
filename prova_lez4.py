class CSVFile():
    
    def __init__(self,name,surname):

        self.nome = name
        self.cognome = surname

    def __str__(self):
        return 'Person "{} {}"'.format(self.name, self.surname)


person = Person('Mario', 'Rossi')
print(person)


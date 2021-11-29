class Automobile():
    def __init__(self, casa_automo, modello, numero_posti, targa):
        self.casa_automo = casa_automo
        self.modello = modello
        self.numero_posti = numero_posti
        self.targa = targa
    
    def __str__(self):
        return "Produttore: {}\nModello: {}\nNumero posti: {}\nTarga: {}".format(self.casa_automo, self.modello, self.numero_posti, self.targa)

    def parla(self):
        print("\"Broom Broom\"")

    def confronta(self, auto2):
        if(self.casa_automo==auto2.casa_automo and self.modello==auto2.modello and self.numero_posti==auto2.numero_posti):
            print("Le due auto sono uguali")
        else:
            print("Le due auto sono diverse")

class Transformer(Automobile):
    def __init__(self, nome, generazione, grado, schieramento):
        self.casa_automo = nome
        self.modello = generazione
        self.numero_posti = grado
        self.targa = schieramento
    
    def scheda_militare(self):
        return "Nome Transformer: {}\nGenerazione: {}\nGrado militare: {}\nFazione: {}".format(self.casa_automo, self.modello, self.numero_posti, self.targa)
    
    def confronta(self, transformerB):
        if(self.casa_automo==transformerB.casa_automo and self.modello==transformerB.modello and self.numero_posti==transformerB.numero_posti):
            print("I due transformers sono uguali, perciò")
        else:
            print("I due transformers sono diversi, perciò")
        super().confronta(transformerB)
        
auto1 = Automobile('Alfa Romeo', '33 Stradale', '2', 'PN 256 IT')
auto2 = Automobile('Alfa Romeo', '33 Stradale', '2', 'TS 789 IT')
auto3 = Automobile('BMW', 'M5', '4', 'RM 384 IT')

print(auto1.__str__())

auto1.parla()

auto1.confronta(auto2)
auto1.confronta(auto3)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

transformer1 = Transformer('Optimus Prime', 'Gen 1', 'Capitano', 'Autobot')
transformer2 = Transformer('Optimus Prime', 'Gen 1', 'Capitano', 'Autobots_')
transformer3 = Transformer('Grimlock', 'Gen 1', 'Leader', 'Dinobot')

print(transformer1.scheda_militare())

transformer1.parla()

transformer1.confronta(transformer2)
transformer1.confronta(transformer3)






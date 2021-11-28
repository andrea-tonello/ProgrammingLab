class Automobile():
    def __init__(self, casa_automo, modello, numero_posti, targa):
        self.casa_automo = casa_automo
        self.modello = modello
        self.numero_posti = numero_posti
        self.targa = targa
    
    def __str__(self):
        return "Produttore: {}\nModello: {}\nNumero posti: {}\nTarga: {}".format(self.casa_automo, self.modello, self.numero_posti, self.targa)

    def parla(self):
        print("Broom Broom")

    def confronta(self, auto2):
        if(self.casa_automo==auto2.casa_automo and self.modello==auto2.modello and self.numero_posti==auto2.numero_posti):
            print("Le due auto sono uguali")
        else:
            print("Le due auto sono diverse")
        

auto1 = Automobile('Alfa Romeo', '33 Stradale', '2', 'PN 256 IT')
auto2 = Automobile('Alfa Romeo', '33 Stradale', '2', 'TS 789 IT')
auto3 = Automobile('BMW', 'Serie 3', '2+2', 'RM 384 IT')

print(auto1.__str__())

auto1.parla()

auto1.confronta(auto2)
auto1.confronta(auto3)



import random

class Automa():
    
    def biancheria(self):
        self.biancheria = None
        if self.biancheria:
            self.biancheria = True
            return 1
        else
            return 0
        

    def calzini(self):
        self.calzini = None
    
    def maglia(self):
        self.maglia = None

    def pantaloni(self):
        self.pantaloni = None

    def scarpe(self):
        self.scarpe = None



automa = Automa()
vestiti = ['b', 'c', 'm', 'p', 's']

pick = random.choice(vestiti)
if pick == 'b':
    automa.biancheria()

automa.calzini
automa.maglia
automa.pantaloni
automa.scarpe

































def esegui (automa, capo):
    
    automa = Automa()

    if capo[0] == a:
        automa.biancheria(capo)
    elif capo[0] == b:
        automa.calzini(capo)
    elif capo[0] == c:
        automa.maglia(capo)
    elif capo[0] == d: 
        automa.pantaloni(capo)
    elif capo[0] == e:
        automa.scarpe(capo)
        

    pass

capi_vestiario = [['a-Mutande di spongebob'],['b-Calzini di Cars 2'], ['c-Maglia del PDL'], ['d-Pantaloni smerdati'], ['e-Crocs']]

automa_1 = Automa()


vestito = True
while(vestito):
    
    pick = random.choice(capi_vestiario)
    esegui(automa_1, pick)


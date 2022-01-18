def convert_and_check (n):
    if type(n) == str:
        
        try:
            if '/' in n:
                
                try:
                    num, denom = n.split('/')
                    num = float(num)
                    denom = float(denom)
                    n = num/denom
                    return n
                except ZeroDivisionError:
                    print('The input number does not exist')
                    exit()
                except Exception:
                    print('Numerical fraction not identified:')
                    
            n = float(n)
            return n
        
        except Exception:
            print('Error: could not convert data')
            exit()
    else:
        return n

def integer(n):
    if n == int(n):
        return True
    else:
        return False

class Calcolatrice():

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.a = convert_and_check(self.a)
        self.b = convert_and_check(self.b)
        
    def sum(self):
        return self.a + self.b

    def subt(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return 'Division by 0 is not allowed'
        
    def power(self):
        if integer(self.a) == True and integer(self.b) == True:
            return pow(self.a, self.b)
        else:
            return 'Cannot calculate a floating point power'

    def root(self):
        if self.a < 0:
            return 'Cannot calculate roots with a negative base '
        if self.b < 1.0 and self.b > 0.0:
            return round(pow(self.a, self.b), 3)
        else:
            return 'You need a rational number between 0 and 1 in order to take the root!'
        
    def module(self):
        return self.a % self.b

    def basechange(self):
        if self.b != 2:
            return 'Only base 2 conversions are allowed'
        else :
            res = []
            while (self.a >= 1):
                res.append(int(self.a % self.b))
                self.a = self.a // self.b
            return f'{res}'


print('-----------------------------------------\nCalcolatrice 1.0\n Che operazione si vuole effettuare? ->\n')

print('A - Addizione\nB - Sottrazione\nC - Moltiplicazione\nD - Divisione\nE - Potenza\nF - Radice\nG - Modulo\nH - Base binaria\n')

op = input()

if op == 'a':
    print('Inserire i numeri da sommare:\n')
    a = input()
    b = input()
    obj = Calcolatrice(a, b)
    print(f'{a} + {b} = {obj.sum()}')
elif op == 'b':
    print('Inserire i numeri da sottrarre:\n')
    a = input()
    b = input()
    obj = Calcolatrice(a, b)
    print(f'{a} - {b} = {obj.subt()}')
elif op == 'c':
    print('Inserire i numeri da moltiplicare:\n')
    a = input()
    b = input()
    obj = Calcolatrice(a, b)
    print(f'{a} * {b} = {obj.mult()}')
elif op == 'd':
    print('Inserire i numeri da dividere:\n')
    a = input()
    b = input()
    obj = Calcolatrice(a, b)
    print(f'{a} / {b} = {obj.div()}')
elif op == 'e':
    print('Inserire base ed esponente:\n')
    a = input()
    b = input()
    obj = Calcolatrice(a, b)
    print(f'{a} ^ {b} = {obj.power()}')
elif op == 'f':
    print('Inserire radice e radicando compreso tra 0 e 1:\n')
    a = input()
    b = input()
    obj = Calcolatrice(a, b)
    print(f'radice {b} di {a} = {obj.root()}')
elif op == 'g':
    print('Inserire base e modulo:\n')
    a = input()
    b = input()
    obj = Calcolatrice(a, b)
    print(f'{a} modulo {b} = {obj.module()}')
elif op == 'h':
    print('Inserire numero e base di arrivo:\n')
    a = input()
    b = input()
    obj = Calcolatrice(a, b)
    print(f'{a} in base {b} = {obj.basechange()}')




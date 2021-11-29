class Stos():
    def __init__(self,stos=[]):
        self.stos=stos
        self.dlugosc=len(stos)

    def pop(self):
        self.stos=self.stod[:len(stos)-2]
        self.dlugosc = self.dlugosc-1

    def push(self,dodaj):
        self.stos.append(dodaj)

    def nieparzyste(self):
        lista=[]
        for i in self.stos:  #iteruje po stosie i wybiera liczby nieparzyste
            if i%2==1:
                lista.append(i)
                print(i)
        for i in lista:  #Usuwa ze stosu liczby nieparzyste
            self.stos.remove(i)
        for i in lista:  #dodaje do stosu liczby nieparzyste
            self.push(i)
        return self.stos  #Zwraca stos

    def get_stos(self):
        return self.stos

stos=Stos()
for i in range(20):
    stos.push(i)
print(stos.get_stos())
print(stos.nieparzyste())




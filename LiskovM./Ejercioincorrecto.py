from abc import ABC, abstractmethod;
@abstractmethod

class Ave(ABC):
    def volar(self):
        pass
    def comer(self):
        pass
    def nadar(self):
        
class Aguila(Ave):
    def volar(self):
        print("Aguila está volando")
    def comer(self):
        print("Aguila está comiendo")
    def nadar(self):
        raise Exception("Las Agulilas no nadan")
    
class Paloma(Ave):
    def volar(self):
        print("Paloma está volando")
    def comer(self):
        print("Paloma está comiendo")
    def nadar(self):
        raise Exception("Las Palomas no nadan")
    
class Pinguino(Ave):
    def volar(self):
        raise Exception("Los pinguinos no vuelan")
    def comer(self):
        print("Pinguino está comiendo")
    def nadar(self):
        print("Los pignuinos estan nadando")
        
a1 = Aguila()
pa1 = Paloma()
p1 = Pinguino()


a1.comer()
a1.volar()
pa1.volar()
p1.volar()
p1.comer()

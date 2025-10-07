from abc import ABC, abstractmethod

class Ave(ABC):
    @abstractmethod
    def comer(self):
        pass
    def respirar(self):
        pass
    
class AveVoladora(Ave):
    @abstractmethod
    def volar(self):
        pass

class AveNadadora(Ave):
    @abstractmethod
    def nadar(self):
        pass
    
class Aguila(AveVoladora):
    def comer(self):
        print("El aguila esta comiendo")
    def respirar(self):
        print("El aguila esta respirando")
    def volar(self):
        print("El aguila está volando")
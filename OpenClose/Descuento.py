class Descuento(ABC):
    @abstractmethod
    def aplicar(self,  precio: float) -> float:
        pass    
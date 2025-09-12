from Descuento import Descuento
class CalculadoraDescuento:
    def __init__(self, descuento: Descuento):
        self.descuento = descuento

    def calcular(self, precio: float) -> float:
        return self.descuento.aplicar(precio)
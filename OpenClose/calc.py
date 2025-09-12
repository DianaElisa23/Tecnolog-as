from DescuentoNavidad import DescuentoNavidad
from DescuentoClienteFrecuente import DescuentoClienteFrecuente
from CalculadoraDescuento import CalculadoraDescuento   

calc = CalculadoraDescuento()

print("Navidad: ", calc.calcular(1000, DescuentoNavidad()))
print("cliente frecuente: ", calc.calcular(1000, DescuentoClienteFrecuente()))
print("Descuento unico: ", calc.calcular(1000, DescuentoUnico()))
import csv

class ManejadorDatos: 
    def __init__(self, archivo):
        self.archivo = archivos
        self.inventario = self._cargar()
    
    def _cargar(self) -> dict:
        with open(self.archivo, "r", newline="") as file:
            lector = csv.reader(f)
        return {fila[0]: fila[1] for fila in lector}
    
    def guardar(self):
        with open(self.archivo, "w", newline=""):
            
def calcular_descuento(tipo: str, precio: float) -> float:
   if tipo == "Navidad":
       return precio * 0.90
   elif tipo == "cliente_frecuente":
        return precio * 0.80
   elif tipo == "descuento_unico":
       return precio * 0.70
   else:
       return precio 


print("Navidad: ", calcular_descuento("Navidad", 1000))
print("cliente frecuente: ", calcular_descuento("cliente_frecuente"))
print("Descuento unico: ", calcular_descuento("descuento_unico"))
class logger:
    def __init__(self):
        self.logs = []
        
    def log(self, mensaje: str) -> None:
        sefl._logs.append(datetime.strftime("%Y - %m. %d%H: %M"))
        
class Usuario:
    def __init__(self, usuario_id:int, nombre: str):
        self.id = usuario_id
        self.nombre = nombre
        self.pedidos = list["Pedido"] = []
        self.logger= logger()
        
    def registrar(self) -> None:
        self.logger.log(f"Usuario{self.nombre} registrado")
        
    def agregar_pedido(self, pedido: "Pedido") -> None:
        self.pedidos.append(pedido)
        self.logger.log(f"Pedido {pedido.id} agregado al usuario {self.nombre}. ")
        
    def get_pedidos(Self) -> list["Pedido"]:
        return self.pedidos
    
    
class Pedido:
    def __init__ 
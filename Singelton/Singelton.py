class logger:
    _instance = None
    _logs: list[str] = []
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def log(Self, mensaje: str) -> None:
        self._logs.append(f"[{datetime.now(.stftime)}]")
        
    def show_logs(Self) -> list[str]:
        return self_.logs
    
class Usuario: 
    def __init__(self, usuario_id: int, nombre: str):
        sel
        
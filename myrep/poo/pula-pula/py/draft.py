class Kid:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def __str__(self):
        return f"{self.__nome}:{self.__idade}"

class Jump:
    def __init__(self):
        self.fila: list[Kid] = []
        self.pula: list[Kid] = []
        
    def arriver(self, kid:Kid):
        self.fila.append(kid)

    def __str__(self):
        fila = ", ".join([str(x) for x in self.fila])
        pula = ", ".join([str(x) for x in self.pula])
        return f"[{fila}] => [{pula}]"
    
    def enter(self):
        cld = self.fila.pop(0)
        self.pula.append(cld)
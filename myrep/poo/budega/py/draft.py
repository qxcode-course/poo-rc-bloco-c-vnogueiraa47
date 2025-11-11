class Cliente:
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def __str__(self):
        return self.__nome
    
class Market:
    def __init__(self, qtdeCaixas: int ):
        self.caixas: list[ Cliente | None] = []
        self.espera: list [ Cliente ] = []
        for _ in range(qtdeCaixas):
            self.caixas.append(None)
    
    def enter(self, cliente: Cliente):
        self.espera.append(cliente)
    
    def call(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("index invalido")
            return
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
            return
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return
        
        self.caixas[index] = self.espera[0]
        del self.espera[0]

    def finish(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print('fail: caixa inexistente')
            return None
        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return None
        aux = self.caixas[index]
        self.caixas[index] = None
        return aux
    
    def __str__(self):
        caixas = ", ".join([str(x) if x else "-----" for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"

def main():
    mercantil = None

    while True:
        line = input()
        print("$" + line)
        args = line.split()
        command = args[0]

        if command == "end":
            break
        elif command == "init":
            mercantil = Market(int(args[1]))
        elif command == "show":
            print(mercantil)
        elif command == "arrive":
            nome = args[1]
            cliente = Cliente(nome)
            mercantil.enter(cliente)
        elif command == "call":
            indice = int(args[1])
            mercantil.call(indice)
        elif command == "finish":
            indice = int(args[1])
            mercantil.finish(indice)
main()
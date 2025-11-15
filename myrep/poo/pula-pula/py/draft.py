class Kid:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def __str__(self):
        return f"{self.__nome}:{self.__idade}"
    
    def getNome(self):
        return self.__nome

class Jump:
    def __init__(self):
        self.fila: list[Kid] = []
        self.pula: list[Kid] = []
        
    def arrive(self, kid:Kid):
        self.fila.insert(0,kid)

    def __str__(self):
        fila = ", ".join([str(x) for x in self.fila])
        pula = ", ".join([str(x) for x in self.pula])
        return f"[{fila}] => [{pula}]"
    
    def enter(self):
        cld = self.fila.pop()
        self.pula.insert(0,cld)

    def leave(self):
        if self.pula:
            cld = self.pula.pop()
            self.fila.insert(0,cld)

    def remove(self,name: str):
        nome = name
        for kid in self.fila:
            if kid.getNome() == name:
                self.fila.remove(kid)
                return
        for kid in self.pula:
            if kid.getNome() == name:
                self.pula.remove(kid)
                return
        if nome not in self.pula:
            print(f"fail: {nome} nao esta no pula-pula")
            
def main():
    pula = Jump()

    while True:
        line = input()
        print("$" + line)
        args = line.split()
        command = args[0]

        if command == "end":
            break
        elif command == "show":
            print(pula)
        elif command == "arrive":
            nome = args[1]
            idade = args[2]
            kid = Kid(nome, idade)
            pula.arrive(kid)
        elif command == "enter":
            pula.enter()
        elif command == "leave":
            pula.leave()
        elif command == "remove":
            crianca = args[1]
            pula.remove(crianca)

main()
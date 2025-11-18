class Client:
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__phone = phone
    def getId(self):
        return self.__id 
    def getPhone(self):
        return self.__phone
    def setId(self, Id: str):
        self.__id = Id
    def setPhone(self, Phone: int):
        self.__phone = Phone
    def __str__(self):
        return f"{self.__id}:{self.__phone}"
    
class Theater:
    def __init__(self, capacidade: int):
        self.__seats: list[ Client | None] = [None] * capacidade
    
    def __str__(self):
        if not self.__seats:
            return f"[]"
        else:
            seats = " ".join([str(x) if x else "-" for x in self.__seats])
            return f"[{seats}]"
        
    def getSeat(self):
        return self.__seats

    
    def __search(self, nome: int):
        for i in range(len(self.__seats)):
            if self.__seats[i] is not None:
                if self.__seats[i].getId() == nome:
                    return i
        return -1
    
    def __verifyIndix(self, index: int):
        if index < 0 or index >= len(self.__seats):
            return False
        
        return True      

    def reserve(self, id: str, cadeira: int,index: int):
        if self.__verifyIndix(index) == False:
            print("fail: cadeira nao existe")
            return
        if self.__search(id) != -1:
            print("fail: cliente ja esta no cinema")
            return
        if self.__seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return
        client = Client(id, cadeira)
        
        self.__seats[index] = client
    
    def cancel(self, id: str):
        if self.__search(id) == -1:
            print("fail: cliente nao esta no cinema")
            return
        
        self.__seats[self.__search(id)] = None

def main():
    cinema = Theater(0)

    while True:
        line = input()
        print("$" + line)
        args = line.split()
        command = args[0]

        if command == "end":
            break

        elif command == "init":
            capacidade = int(args[1])
            cinema = Theater(capacidade)

        elif command == "show":
            print(cinema)

        elif command == "reserve":
            id = args[1]
            phone = int(args[2])
            indice = int(args[3])
            cinema.reserve(id, phone, indice)
        
        elif command == "cancel":
            id = args[1]
            cinema.cancel(id)

main()



            
    












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    



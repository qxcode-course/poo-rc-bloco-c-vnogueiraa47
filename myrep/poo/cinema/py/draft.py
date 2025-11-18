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
    
    def reserve(self, client: Client, index: int):
            if index < 0 or index >= len(self.__seats):
                print("fail: cadeira nao existe")
                return
            if self.__seats[index] is not None:
                print("fail: cadeira ja esta ocupada")
                return
            if client in self.__seats:
                
                print("fail: cliente ja esta no cinema")
                return
            
            self.__seats[index] = client
    
    
    def cancel(self,client: Client):
        if client not in self.__seats:
            print("fail: cliente nao esta no cinema")
            return
        
        self.__seats.remove(client)

def main():
    cinema  = Theater(0)

    while True:
        line = input()
        print("$" + line)
        args = line.split()
        command = args[0]

        if command == "end":
            break
        elif command == "init":
            cinema = Theater(int(args[1]))
        elif command == "show":
            print(cinema)
        elif command == "reserve":
            id = args[1]
            phone = args[2]
            indice = int(args[3])
            client = Client(id, phone)
            cinema.reserve(client, indice)
        elif command == "cancel":
            client = args[1]
            cinema.cancel(client)
main()
    



    



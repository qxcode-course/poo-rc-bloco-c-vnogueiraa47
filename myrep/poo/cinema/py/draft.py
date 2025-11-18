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
            if self.cadeiras[i] is not None:
                if self.__seats[i].getId() == nome:
                    return i
        return -1
    
    def __verifyIndix(self, index: int):
        if index < 0 or index >= len(self.__seats):
            return False
        
        return True      

            
    












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    



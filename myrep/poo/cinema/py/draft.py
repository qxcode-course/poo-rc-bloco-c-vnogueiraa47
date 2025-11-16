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
        return f"{self.__id} : {self.__phone}"
    
class Theater:
    def __init__(self, capacidade: int):
        self.__seats: list[ Client | None] = [None] * capacidade
    
    def str(self):
        
class Cliente:
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def _str__(self):
        return self.__nome
    
class Market:
    def __init__(self, qtdeCaixas: int ):
        self.caixas = list[ Cliente | None] = []
        self.espera = list [ Cliente ] = []
        for _ in range(qtdeCaixas):
            self.caixas.append(None)


        
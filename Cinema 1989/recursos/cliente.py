from recursos.pessoa import Pessoa

class Cliente(Pessoa):
    __id = None  
    
    def __init__(self, *args, **kwargs):
        super().__init__()

    def setID(self, id):
        self.__id = id
        return 
        
    def getID(self):
        return self.__id
    
    def getDados(self):
        dados = super().getDados()
        dados['id'] = self.__id
        return dados

    def __str__(self):
        return self.nome
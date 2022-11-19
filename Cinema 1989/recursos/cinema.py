class Cinema:
    # Controle de IDs
    __last__cliente_id = -1
    __last__sessao_id = -1
    __last__filme_id = -1

    def __init__(self, nome, numero_sessoes, aberto=True):
        self.nome = nome
        self.__numero_sessoes = numero_sessoes
        self.__aberto = aberto 
    
    def gerarClienteID(self, cliente):
        cliente_id = self.__last__cliente_id + 1
        self.__last__cliente_id= cliente_id
        cliente.setID(cliente_id)
    
    def gerarSessaoID(self, sessao):
        sessao_id = self.__last__sessao_id + 1
        self.__last__sessao_id = sessao_id
        sessao.setID(sessao_id)

    def gerarFilmeID(self, filme):
        filme_id = self.__last__filme_id + 1
        self.__last__filme_id = filme_id
        filme.setID(filme_id)
  
    def getSituacao(self):
        return self.__aberto

    def setSituacao(self, situacao):
        self.__aberto = situacao

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getNumeroSessoes(self):
        return self.__numero_sessoes

    def setNumeroSessoes(self, numero):
        self.__numero_sessoes = numero
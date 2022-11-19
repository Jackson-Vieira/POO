from recursos.sessao import Sessao
from recursos.filme import Filme
from recursos.cliente import Cliente

class DataBase:
    def __init__(self, cinema):
        self.cinema = cinema

    clientes = []
    sessoes = []
    filmes = []

    def addCliente(self, dados):
        cliente = Cliente()
        cliente.setDados(dados=dados)
        self.cinema.gerarClienteID(cliente=cliente)
        self.clientes.append(cliente)

    def getClientes(self):
        return self.clientes

    def addSessao(self, localizacao):
        sessao = Sessao(localizacao)
        self.cinema.gerarSessaoID(sessao=sessao)
        self.sessoes.append(sessao)
        
    def getSessao(self):
        pass

    def getSessoes(self):
        return self.sessoes
 
    def addFilme(self, dados):
        filme = Filme()
        filme.setDados(dados=dados)
        self.cinema.gerarFilmeID(filme=filme)
        self.filmes.append(filme)
        
    def getFilme(self, id):
        pass

    def getFilmes(self):
        return self.filmes
class Filme:
    __id = None
    titulo = ''
    diretor = 'diretor'
    ano_lacamento = 0
    avaliacao_imdb = 0

    def getDados(self):
        dados = {
            "titulo":self.titulo,
            "diretor": self.diretor,
            "ano_lacamento": self.ano_lacamento,
            "avaliacao_imdb": self.avaliacao_imdb,
        }
        return dados

    def setDados(self, dados):
        titulo =  dados.get("titulo")
        diretor = dados.get("diretor")
        ano_lacamento = dados.get("ano_lacamento")
        avaliacao_imdb = dados.get("avaliacao_imdb")
        # validação (dados obrigatórios, validação do ano)
        self.titulo = titulo
        self.diretor = diretor
        self.ano_lacamento = ano_lacamento
        self.avaliacao_imdb = avaliacao_imdb

    def setID(self, id):
        self.__id = id
        return 
        
    def getID(self):
        return self.__id

    def __str__(self):
        return self.titulo
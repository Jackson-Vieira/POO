import uuid

class Sessao:
    NUMERO_CADEIRAS = 24
    __id = None

    __aberta = False
    __filme = None
    __horario = None
    __data = None

    def __init__(self, localizacao):
        self.localizacao = localizacao
        self.__bilhetes = self._gerarBilhetes()
        self.__cadeiras_disponiveis = [
            ['00', '01', '02', '03',],
            ['10', '11', '12', '13',],
            ['20', '21', '22', '23',],
            ['30', '31', '32', '33',],
            ['40', '41', '42', '43',],
            ['50', '51', '52', '53',],
        ]
        self.__bilhetes_esgotados = False
        self.__num_bilhetes_disponiveis = 24

    def __verificarCadeira(self, cod_cadeira):
        linha = int(cod_cadeira[0])
        coluna = int(cod_cadeira[1:])
        return False if self.__cadeiras_disponiveis[linha][coluna] == 0 else True

    def __atualizarSituacao(self):
        if self.__num_bilhetes_disponiveis == 0:
            self.__bilhetes_esgotados = True

    def _gerarBilhetes(self):
        return [str(uuid.uuid4()) for b in range(self.NUMERO_CADEIRAS)]

    def __getBilhetes(self):
        return self.__bilhetes
    
    def _setDados(self, dados):
        filme = dados.get("filme")
        horario = dados.get("horario")
        data = dados.get("data")

        self.__filme = filme
        self.__horario = horario
        self.__data = data

    def abrirSessao(self, dados):
        self._setDados(dados)
        self.__aberta = True
        print("Sessão criada com sucesso!")

    def fecharSessao(self):
        self.__aberta = False

    def comprarBilhete(self, cod_cadeira):
        if self.__verificarCadeira(cod_cadeira) and not self.__bilhetes_esgotados and self.__aberta: # and tem bilhete disponivel
            linha = int(cod_cadeira[0])
            coluna = int(cod_cadeira[1])
            self.__cadeiras_disponiveis[linha][coluna] = 0
            index_bilhete = self.__num_bilhetes_disponiveis-1
            self.__num_bilhetes_disponiveis -= 1
            self.__atualizarSituacao()
            bilhete = self.__getBilhetes()[index_bilhete]
            return f"Ação realizada com sucesso!\nN° Bilhete: {bilhete}"
        return f"\nNão foi possível realizar a ação!\nPossíveis motivos:\n  - Bilhetes esgotados\n  - Sessão fechada"
            
    def getDados(self):
        dados = {
            "id": self.__id,
            "localizacao":self.localizacao,
            "quantidade_cadeiras":self._quantidade_cadeiras,
            "aberta":self.__aberta,
            "filme":self.__filme,
            "horario":self.__horario,
            "data":self.__data,
        }
        return dados

    def getCadeirasDisponiveis(self):
        return self.__cadeiras_disponiveis

    def getID(self):
        return self.__id
    
    def setID(self, id):
        self.__id = id

    def __str__(self):
        return self.localizacao
class Pessoa:
    nome = ''
    __data_nascimento = ''
    __cpf = ''

    def getDados(self):
        dados = {
            "nome":self.nome,
            "data_nascimento":self.data_nascimento,
            "cpf": self._cpf
        }
        return dados
    
    def _validarDados(self, nome, data_nascimento, cpf):
        return nome and cpf and data_nascimento

    def setDados(self, dados):
        nome = dados.get("nome")
        data_nascimento  = dados.get("data_nascimento")
        cpf = dados.get("cpf")
        if self._validarDados(nome, data_nascimento, cpf):
            self.nome = nome
            self.__data_nascimento = data_nascimento
            self.__cpf = cpf
            print("\nCLIENTE CRIADO COM SUCESSO!\n")

        else:
            print("\nNÃO FOI POSSIVEL REALIZAR A AÇÃO!\n")

    def __str__(self):
        return self.nome
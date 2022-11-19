from utils import limparTerminal
from population import population

class Manager:
    def __init__(self, database, cinema):
        self.database = database
        self.cinema = cinema

    def _comprarBilhete(self):
        sessao_id = int(input("Sessão ID: "))
        self._mostrarCadeiras(sessao_id=sessao_id)
        cod_cadeira = input("Código cadeira: ")
        sessao = self.database.getSessoes()[sessao_id]
        print(sessao.comprarBilhete(cod_cadeira))

    def _addCliente(self):
        print("\n--- CADASTRAR CLIENTE ---")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nascimento = input("Data nascimento: ")

        #validação dos dados
        dados = {
            "nome":nome,
            "cpf":cpf,
            "data_nascimento":data_nascimento
        }
        self.database.addCliente(dados=dados)

    def _addSessao(self):
        print("\n--- CADASTRAR SESSÃO ---")
        localização = input("Localização: ")
        self.database.addSessao(localização)

    def _abrirSessao(self):
        print("\n--- ABRIR SESSÃO --- ")
        sessao_id = int(input("Sessão ID: "))
        sessao = self.database.getSessoes()[sessao_id]
        filme_id = int(input("Filme ID: "))
        horario = input("Horário inicio: ")
        data = input("Data inicio: ")
        
        #validação dos dados
        filme_data = self.database.getFilmes()[filme_id].getDados()

        dados = {
            "filme": filme_data,
            "horario": horario,
            "data":data,
        }
        sessao.abrirSessao(dados)
        
    def _addFilme(self):
        print("\n--- CADASTRAR FILME ---")
        titulo = input("Titulo: ")
        diretor = input("Diretor: ")
        ano_lacamento = int(input("Ano laçamento: "))
        avaliacao_imdb = int(input("Avaliação IMDB: "))
        dados = {
            "titulo": titulo,
            "diretor":diretor,
            "ano_lacamento": ano_lacamento,
            "avaliacao_imdb":avaliacao_imdb
        }
        self.database.addFilme(dados)


    def _listarFilmes(self, orderned_by_year=False, orderned_by_avaliacao=False):
        filmes = self.database.getFilmes()

        if orderned_by_year:
            def greater_year(x):
                return x.ano_lacamento
            filmes = sorted(filmes,  key=greater_year, reverse=True)

        elif orderned_by_avaliacao:
            def greater_avaliacao(x):
                return x.avaliacao_imdb
            filmes = sorted(filmes, key=greater_avaliacao, reverse=True)

        print("ID - FILME  -  AVALIAÇÃO - ANO LAÇAMENTO")
        for i, filme in enumerate(filmes):
            filme_id = filme.getID()
            print(f'{filme_id} | {filme} | {filme.avaliacao_imdb} | {filme.ano_lacamento}')

    def _listarSessoes(self):
        print("ID - LOCALIZAÇÃO SESSÃO")
        sessoes = self.database.getSessoes()
        for i, sessao in enumerate(sessoes):
            print(i, sessao)

    def _mostrarCadeiras(self, sessao_id=None):
        if sessao_id == None:
            sessao_id = int(input("Sessão ID: "))

        try:
            sessao = self.database.getSessoes()[sessao_id]
            cadeiras = sessao.getCadeirasDisponiveis()

        except:
            print("ID inválido!")
            return

        cod_insdiponivel = "[X]"
        n = len(cadeiras)
        print(f"\n--- CADEIRAS SESSÃO - {sessao.getID()}---")
        for i in range(n):
            for k in range(len(cadeiras[0])):
                cadeira = cadeiras[i][k]
                if cadeira == 0:
                    print(" "+cod_insdiponivel, end=" ")
                else:
                    print(f"[{cadeira}]", end=" ")
            print()


    def _bloco_informacoes(self):
        print("\n1- Lista de Filmes\n2- Lista de Sessões\n3- Mostrar Cadeiras Disponíveis\n5- Voltar")
        opcao = int(input("-- "))
        if opcao == 1:
            print("\n-- OPÇÕES FILMES --\n")
            print("1- Catálogo de Filmes\n2- Listar Filmes Melhores Avaliados\n3- Listar Filmes Mais Recentes\n")
            opcao = int(input('-- '))
            if opcao == 1:
                self._listarFilmes()
            elif opcao == 2:
                self._listarFilmes(orderned_by_avaliacao=True)
            elif opcao == 3:
                self._listarFilmes(orderned_by_year=True)
            else:
                print("Opção inválida!")

        elif opcao == 2:
            self._listarSessoes() 
        elif opcao == 3:
            self._mostrarCadeiras()
        elif opcao == 5:
            self.home()

        self._bloco_informacoes()
        

    def _bloco_operacoes(self):
        print("\n0- Comprar Bilhete\n1- Registrar Cliente\n2- Registrar Sessão\n3- Registrar Filme\n4- Abrir Sessão\n5- Voltar")
        opcao = int(input("-- "))
        if opcao == 0:
            self._comprarBilhete()
        if opcao == 1:
            self._addCliente()
        if opcao == 2:
            self._addSessao()
        if opcao == 3:
            self._addFilme()
        if opcao == 4:
            self._abrirSessao()
        if opcao == 5:
            self.home()
        else:
            pass
        self._bloco_operacoes()

    def _bloco_validacoes(self):
        print("\nEssa área ainda não está disponível!\n")

    def home(self):
        limparTerminal()
        print(f"CINEMA - {self.cinema.nome}")
        print("\n1- Informações (Leitura)\n2- Operações (Ações)\n3- Validações\n")
        opcao = int(input("-- "))
        if opcao == 1:
            self._bloco_informacoes()
        elif opcao == 2:
            self._bloco_operacoes()
        elif opcao == 3:
            self._bloco_validacoes()
        elif opcao == 444:
            population(self.database)
        else:
            print("Opção inválida!")
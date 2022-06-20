from Resource.Models.Produto import Produto
from Resource.Views.ProdutoTela import ProdutoTela


class ProdutoController:
    def __init__(self, sistema):
        self.__tela_produto = ProdutoTela(self)
        self.__lista_produtos = []
        self.__lista_qualificadores = []
        self.__sistema = sistema
        self.__menu_opcoes = {
            'Cadastrar Produto': self.criar_produto,
            'Listar Produtos': self.listar_produtos,
            'Alterar Produto': self.alterar_produto,
            'Excluir Produto': self.excluir_produto,
            'Adicionar Preço': self.adicionar_preco_produto,
            'Ver Preços': self.ver_precos_produto,
            'Colaborar com Preços': self.colaborar_precos_produtos,
            'Excluir Preço': self.excluir_preco_produto,
            'Voltar': self.voltar
        }
        self.__ON = True

    # GETTERS
    @property
    def tela_produto(self):
        return self.__tela_produto

    @property
    def lista_produtos(self):
        return self.__lista_produtos

    @property
    def lista_qualificadores(self):
        return self.__lista_qualificadores

    @property
    def sistema(self):
        return self.__sistema

    @property
    def ON(self):
        return self.__ON

    # CRUD
    def criar_produto(self):
        self.__tela_produto.exibir_mensagem('FORMULÁRIO DE PRODUTO: ')
        dados_produto = self.__tela_produto.cadastrar_produto_formulario()
        novo_produto = Produto(
            dados_produto['nome'],
            dados_produto['descricao'],
            dados_produto['qualificadores']
        )
        self.adicionar_produto_lista(novo_produto)
        self.__tela_produto.exibir_mensagem("Produto cadastrado com sucesso!")
        self.__tela_produto.continuar()

    def alterar_produto(self):
        pass

    def excluir_produto(self):
        produto = self.escolher_produto()
        if produto:
            confirma = self.__tela_produto.exibir_confirmacao_exclusao()
            if confirma:
                self.remover_produto_lista(produto)
                self.__tela_produto.exibir_mensagem('Produto excluído com sucesso!')
                self.__tela_produto.continuar()

    def listar_produtos(self):
        self.__tela_produto.exibir_lista_produtos(self.__lista_produtos)
        self.__tela_produto.continuar()

    # OUTROS MÉTODOS
    def editar_preco_produto(self):
        opcao = self.escolher_precos_produtos_por_supermercado()

    def escolher_produto(self):
        produtos = self.__lista_produtos
        opcao = self.__tela_produto.escolher_produto(produtos)
        if opcao != False:
            return produtos[opcao - 1]
        return False

    def escolher_qualificador(self):
        qualificadores = self.__lista_qualificadores
        opcao = self.__tela_produto.escolher_qualificadores(qualificadores)
        if opcao != False:
            return qualificadores[opcao - 1]
        return False

    def escolher_precos_produtos_por_supermercado(self):
        dicionario_produtos = {}
        precos_supermercado = self.__sistema.preco_controller.buscar_precos_supermercados()
        for preco in precos_supermercado:
            valores = dicionario_produtos.get(preco.produto, False)
            if valores:
                dicionario_produtos[preco.produto] = valores.append(preco.valor)
            else:
                dicionario_produtos[preco.produto] = [preco.valor]

        return self.__tela_produto.escolher_produtos_precos_supermercado(dicionario_produtos)

    def adicionar_produto_lista(self, produto):
        if isinstance(produto, Produto):
            if produto not in self.__lista_produtos:
                self.__lista_produtos.append(produto)

    def remover_produto_lista(self, produto):
        if isinstance(produto, Produto):
            if produto in self.__lista_produtos:
                self.__lista_produtos.remove(produto)

    def listar_qualificadores(self):
        self.__tela_produto.exibir_lista_qualificadores(self.__lista_qualificadores)
        self.__tela_produto.continuar()

    def excluir_qualificador(self):
        qualificador = self.escolher_qualificador()
        if qualificador:
            confirma = self.__tela_produto.exibir_confirmacao_exclusao()
            if confirma:
                if qualificador in self.__lista_qualificadores:
                    self.__lista_qualificadores.remove(qualificador)
                    self.__tela_produto.exibir_mensagem('Qualificador excluído com sucesso!')
                    self.__tela_produto.continuar()

    def adicionar_preco_produto(self):
        self.__tela_produto.exibir_mensagem('ESCOLHA O PRODUTO QUE DESEJA INFORMAR PREÇO!')
        produto = self.escolher_produto()
        if produto:
            preco  = self.__sistema.preco_controller.criar_preco(produto)
            if preco:
                produto.add_preco(preco)
                self.__sistema.preco_controller.adicionar_preco_lista(preco)
                self.__tela_produto.exibir_mensagem('Preço incluído com sucesso')
            return False
        else:
            return False

    def ver_precos_produto(self):
        self.__tela_produto.exibir_mensagem('ESCOLHA O PRODUTO QUE DESEJA VER OS PREÇOS!')
        produto = self.escolher_produto()
        if produto:
            lista_precos = produto.precos
            if lista_precos:
                self.__sistema.preco_controller.listar_precos(lista_precos)
                return lista_precos
        self.__tela_produto.exibir_mensagem('Não há preços cadastrados')
        self.__tela_produto.continuar()
        return False

    def colaborar_precos_produtos(self):
        self.__tela_produto.exibir_mensagem('PREÇOS DE PRODUTOS POR SUPERMERCADOS!')
        precos = []
        cont = 1
        if len(self.__lista_produtos) > 0:
            for produto in self.__lista_produtos:
                for preco in produto.precos:
                    print(f'{cont} - {produto.nome} | {preco.supermercado.nome} = {preco.valor}')
                    for qualificador in produto.qualificadores:
                        print(f'- {qualificador.nome}')
                    precos.append(preco)
                    cont += 1

            self.__tela_produto.exibir_mensagem('COM QUAL PREÇO QUER CONTRIBUIR?')
            try:
                opcao = int(input('Opção: '));
                if opcao <= len(precos):
                    precos[opcao - 1].confirma_preco()
                    self.__tela_produto.exibir_mensagem('OBRIGADA PELA CONTRIBUIÇÃO!')
                    self.__tela_produto.continuar()
                    return precos[opcao - 1]
                else:
                    raise ValueError('Valor informado maior que o permitido')
            except ValueError:
                print(f'O valor deve ser um número inteiro entre 1 e {len(precos)}')

        return False

    def excluir_preco_produto(self):
        self.__tela_produto.exibir_mensagem('EXCLUIR PREÇO DE PRODUTO!')
        precos = []
        cont = 1
        if len(self.__lista_produtos) > 0:
            self.__tela_produto.exibir_mensagem('QUAL PREÇO QUER EXCLUIR?')
            for produto in self.__lista_produtos:
                for preco in produto.precos:
                    print(f'{cont} - {produto.nome} | {preco.supermercado.nome} = {preco.valor}')
                    for qualificador in produto.qualificadores:
                        print(f'- {qualificador.nome}')
                    precos.append({'preco':preco, 'produto': produto})
                    cont += 1

            try:
                opcao = int(input('Opção: '));
                if opcao <= len(precos):
                    produto = precos[opcao - 1]['produto']
                    preco = precos[opcao - 1]['preco']
                    produto.remove_preco(preco)
                    self.__sistema.preco_controller.remover_preco_lista(preco)
                    self.__tela_produto.exibir_mensagem('Preço excluído com sucesso')
                    self.__tela_produto.continuar()
                else:
                    raise ValueError('Valor informado maior que o permitido')
            except ValueError:
                print(f'O valor deve ser um número inteiro entre 1 e {len(precos)}')

        return False

    def listar_menus(self):
        self.__ON = True
        while self.__ON:
            menu_opcoes = self.__menu_opcoes
            opcao = self.__tela_produto.ver_menu(menu_opcoes)
            if opcao:
                menu_opcoes[opcao]()

    def voltar(self):
        self.__ON = False

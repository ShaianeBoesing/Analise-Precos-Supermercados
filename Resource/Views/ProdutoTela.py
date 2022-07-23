import PySimpleGUI as sg
from Resource.Views.AbstractTela import AbstractTela
from Resource.Exceptions.EmptyStringException import EmptyStringException


class ProdutoTela(AbstractTela):
    def __init__(self, controlador):
        pass

    def cadastrar_produto_formulario(self, categorias):
        lista_cat = []
        for cat in categorias:
            lista_cat.append(cat)

        layout = [
            [sg.Text('-------- DADOS PRODUTO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='descricao')],
            [sg.Text('Qualificadores (2):', size=(15, 1)), sg.InputText('', key='qualificador1')],
            [sg.Text('', size=(15, 1)), sg.InputText('', key='qualificador2')], # inserir opção para escolher qualificadores
            [sg.Text('Categoria:', size=(15, 1)), sg.Combo(lista_cat, key='categoria', size=(15,1))], # inserir opção para escolher categorias
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.window = sg.Window('Cadastramento de Produto').Layout(layout)

        button, response = self.open()
        response['qualificadores'] = [response['qualificador1'],response['qualificador2']]
        self.close()
        if button == "Confirmar":
            return response

        return False

    def exibir_produtos_precos_supermercados(self, produtos: list):
        super().exibir_mensagem("Lista de Produtos e Preços")
        try:
            if len(produtos) > 0:
                i = 0
                lista_produtos = []
                for produto, valores in produtos.items():
                    i += 1
                    print(i, '- ', produto.nome)
                    if len(valores) > 0:
                        for valor in valores:
                            print(' - ', valor)
                    else:
                        print('- nenhum valor informado')
                    lista_produtos.append(produto)
                opcao = int(input('Opção: '))
                return lista_produtos[opcao - 1]
            else:
                print('Não há produtos cadastrados para seu supermercado!')
                super().continuar()
                return False
        except ValueError:
            print('Valor inválido!')
            super().continuar()
            return False

    def escolher_produtos_precos_supermercado(self, produtos):
        produto = self.exibir_produtos_precos_supermercados(produtos)
        if produto:
            return produto
        return False

    def escolher_qualificadores(self):
        continuar = 1
        qualificadores = []
        while continuar:
            try:
                qualificador = input('Qualificador: ')
                if qualificador:
                    qualificadores.append(qualificador)
                else:
                    raise EmptyStringException
                super().exibir_mensagem('Deseja inserir mais um qualificador?')
                print('0- Não')
                print('1- Sim')
                try:
                    continuar = int(input('Opcão: '))
                except ValueError:
                    print('Opção inválida')
                    continuar = 0
            except EmptyStringException as e:
                print(e)

        return qualificadores

    def escolher_categorias(self, categorias):
        try:
            tam_categoria = len(categorias)
            if tam_categoria > 0:
                super().exibir_mensagem('Escolha uma categoria: ')
                for i in range(tam_categoria):
                    print(f'{i+1} - {categorias[i].nome}')
                opcao = int(input('Opção: '))
                if opcao > tam_categoria:
                    raise ValueError
                return categorias[opcao - 1]
            else:
                super().exibir_mensagem('Não há categorias cadastradas')
                return False
        except ValueError:
            print(f'O valor deve ser um número inteiro entre 1 e {tam_categoria}')
            return False


    def editar_qualificador(self):
        continuar = 1
        qualificadores = []
        while continuar:
            try:
                qualificador = input('Qualificador: ')
                if qualificador:
                    qualificadores.append(qualificador)
                else:
                    raise EmptyStringException
                super().exibir_mensagem('Deseja inserir mais um qualificador?')
                print('0- Não')
                print('1- Sim')
                try:
                    continuar = int(input('Opcão: '))
                except ValueError:
                    print('Opção inválida')
                    continuar = 0
            except EmptyStringException as e:
                print(e)

        return qualificadores

    def exibir_lista_produtos(self, produtos):
        total_produtos = len(produtos)
        lista_prod = []
        if total_produtos:
            for prod in produtos:
                lista_prod.append([sg.Text(prod['nome'], font=('Helvica', 18))])
                lista_prod.append([sg.Text(  prod['categoria'] + ' | '
                                           + prod['qualificadores'][0].nome + ' e '
                                           + prod['qualificadores'][1].nome)])
                lista_prod.append([sg.Text('-'*70, size=(15, 1))])

            layout = [
                [sg.Text('LISTA DE PRODUTOS', font=("Helvica", 25))],
                lista_prod,
                [sg.Button('OK')]
            ]
            self.window = sg.Window('Cadastro Produto').Layout(layout)
            self.open()
            self.close()

            return True
        else:
            print('Não há produtos cadastrados!')
            return False

    def exibir_lista_qualificadores(self, qualificadores):
        super().exibir_mensagem("Lista de Qualificadores")
        total_qualificadores = len(qualificadores)

        if total_qualificadores:
            for i in range(total_qualificadores):
                print(i + 1, '- ', qualificadores[i].nome, '|', qualificadores[i].descricao)
                for q in qualificadores[i].qualificadores:
                    print('  -', q.nome)
                print('-' * 71)
            return True
        else:
            print('Não há qualificadores cadastrados!')
            return False

    def escolher_produto(self, produtos):
        try:
            total = len(produtos)
            lista_prod = []
            if total:
                for prod in produtos:
                    lista_prod.append([sg.Radio(prod, "RD2")])

                layout = [
                    [sg.Text('LISTA DE PRODUTOS', font=("Helvica", 25))],
                    lista_prod,
                    [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
                self.window = sg.Window('Escolher Produto').Layout(layout)

                button, response = self.open()
                self.close()
                opcao = [k for k, v in response.items() if v is True]
                print(opcao)
                if button=="Confirmar":
                    if opcao:
                        return opcao[0]
                    self.exibir_mensagem('Opção inválida')
                raise ValueError()
            else:
                self.exibir_mensagem('Não há produtos cadastradas!')
                return None
        except ValueError:
            return None

        except ValueError:
            print(f'O valor precisa ser um número inteiro entre 1 e {total}')
            self.continuar()
            return False


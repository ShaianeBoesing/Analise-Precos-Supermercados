import PySimpleGUI as sg
from Resource.Views.AbstractTela import AbstractTela
from Resource.Exceptions.EmptyStringException import EmptyStringException

class PrecoTela(AbstractTela):
    def __init__(self, controlador):
        self.__controlador = controlador


    def cadastrar_preco_formulario(self, supermercados):
        try:
            lista_supermercados = []
            for sup in supermercados:
                lista_supermercados.append(sup)

            layout = [
                [sg.Text('-------- CADASTRAR PREÇO ----------', font=("Helvica", 25))],
                [sg.Text('Preço:', size=(15, 1)), sg.InputText('', key='valor')],
                [sg.Text('Supermercado:', size=(15, 1)), sg.Combo(lista_supermercados, key='supermercado', size=(15, 1))],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.window = sg.Window('Cadastro Preço').Layout(layout)

            button, response = self.open()
            self.close()
            if button == "Confirmar":
                if (response['valor'] != ''):
                    return response
                raise EmptyStringException

            return False

        except ValueError:
            print('Valor inválido.')
            return False

    def editar_preco_formulario(self):
        try:
            valor = float(input('Preço: R$ '))
            return {'valor': valor}
        except ValueError:
            print('Valor inválido.')
            return False

    def exibir_lista_precos(self, precos):
        total_precos = len(precos)
        lista_preco = []

        if total_precos:
            for preco in precos:
                lista_preco.append([sg.Text('- ' + preco, font=('Helvica', 15))])

            layout = [
                [sg.Text('LISTA DE PREÇOS', font=("Helvica", 25))],
                lista_preco,
                [sg.Button('OK')]
            ]
            self.window = sg.Window('Lista preços').Layout(layout)
            self.open()
            self.close()

            return True
        else:
            return False

    def escolher_produto(self):
        continuar = 1
        produtos = []
        while continuar:
            try:
                produto = input('Produto: ')
                if produto:
                    produtos.append(produto)
                else:
                    raise EmptyStringException
                super().exibir_mensagem('Deseja inserir mais um produto?')
                print('0- Não')
                print('1- Sim')
                try:
                    continuar = int(input('Opcão: '))
                except ValueError:
                    print('Opção inválida')
                    continuar = 0
            except EmptyStringException as e:
                print(e)

        return produtos

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

    def exibir_listas_supermercados(self, supermercados: list):
        super().exibir_mensagem("Lista de Supermercados")
        total_supermercados = len(supermercados)

        if total_supermercados:
            for i in range(total_supermercados):
                print(i + 1, '- ', supermercados[i].nome, ' | ', supermercados[i].endereco)
            return True
        else:
            print('Não há supermercados cadastrados!')
            return False

    def colaborar_precos_formulario(self, precos):
        total_precos = len(precos)
        lista_prec = []
        if total_precos:
            for prec in precos:
                preco = prec['produto'] + prec['supermercado'] + prec['valor']
                lista_prec.append([sg.Checkbox(preco)])

            layout = [
                [sg.Text('Selecione os preços que concorda', font=("Helvica", 25))],
                lista_prec,
                [sg.Button('Confirmar'), sg.Button('Cancelar')]
            ]
            self.window = sg.Window('Colaborar Preços').Layout(layout)

            button, response = self.open()
            self.close()
            selecionados = [k for k, v in response.items() if v is True]
            print(response, selecionados)
            if button == "Confirmar":
                if selecionados:
                    self.exibir_mensagem('Obrigada por contribuir!')
                    return selecionados

            return False
        else:
            self.exibir_mensagem('Não há preços cadastradovs!')
            return False

    def escolher_preco(self, precos):
        try:
            total_precos = len(precos)
            lista_prec = []
            if total_precos:
                for prec in precos:
                    preco = prec['produto'] + prec['supermercado'] + prec['valor']
                    lista_prec.append([sg.Radio(preco, "RD5")])

                layout = [
                    [sg.Text('LISTA DE PREÇOS', font=("Helvica", 25))],
                    lista_prec,
                    [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
                self.window = sg.Window('Escolher Preço').Layout(layout)

                button, response = self.open()
                self.close()
                opcao = [k for k, v in response.items() if v is True]
                if button=="Confirmar":
                    if opcao:
                        return opcao[0]
                    self.exibir_mensagem('Opção inválida')

                raise ValueError()
            else:
                self.exibir_mensagem('Não há preços cadastradas!')
                return None
        except ValueError:
            return None

import PySimpleGUI as sg

layout = [
    [sg.Text('Incluir novo Cliente')],
    [sg.Text('Nome', size=(15, 1)), sg.InputText('nome')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Cadastro de Clientes').Layout(layout)

button, values = window.Read()
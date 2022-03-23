import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import ICON_BUY_ME_A_COFFEE

class UserInterface:
    sg.theme('LightBlue5')   # Add a touch of color
    # All the stuff inside your window.
    layout = [
                [sg.Titlebar(title='Калькулятор', icon=ICON_BUY_ME_A_COFFEE)],
                [sg.InputText(size=(45, 6))],
                [sg.Button('1', size=(8, 4)), sg.Button('2', size=(8, 4)), sg.Button('3', size=(8, 4)), sg.Button('+', size=(8,4))],
                [sg.Button('4', size=(8, 4)), sg.Button('5', size=(8, 4)), sg.Button('6', size=(8, 4)), sg.Button('-', size=(8,4))],
                [sg.Button('7', size=(8, 4)), sg.Button('8', size=(8, 4)), sg.Button('9', size=(8, 4)), sg.Button('/', size=(8,4))],
                [sg.Button('0', size=(28 , 4)), sg.Button('*', size=(8,4))]
            ]
                # [sg.Text('Enter something on Row 2'), sg.InputText()],
                # [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()

class Calc:
    def __init__(self):
        pass
    def add(self ,x: int , y: int ):
        return x + y
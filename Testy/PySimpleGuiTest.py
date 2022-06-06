import PySimpleGUI as sg

sg.theme('DarkTeal')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Image('simple_path.png')],
            [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]  ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    if event == 'Ok':
        print('You entered ', values[1])

window.close()
#Made by me to learn UI all thanks to PySimpleGUI used with the help of: https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms
import PySimpleGUI as pg

pg.theme('darkamber')
layout = [
    [pg.Text("Enter Name:"), pg.InputText('Name')],
    [pg.Text("Enter Last_Name:"), pg.InputText('Last_Name')],
    [
        pg.Input(key='-IL-', size=(20, 1), enable_events=True, pad=(0, (0, 10)), justification='right'),
        pg.CalendarButton('Enter Date', close_when_date_chosen=False, target='-IL-', no_titlebar=True)
    ],
    [pg.Button("Read"), pg.Button("Close" , button_color = 'red')]
]
Window = pg.Window("Register", layout,
                   default_element_size=(13, 1),
                   text_justification='r',
                   auto_size_text=False,
                   auto_size_buttons=False,
                   no_titlebar=False,
                   grab_anywhere=True,
                   default_button_element_size=(12, 1),
                   resizable=True,finalize=True)

while True:
    event, value = Window.read()
    if event == "Close" or event == pg.WIN_CLOSED:
        break
    elif event == "Read":
        if value ['-IL-'] and all(char.isdigit() or char in {'-', ':' , ' '} for char in value['-IL-']): #checks for the correct date

            pg.popup('Sucessfuly registered')

            # Save the information to a file
            with open("user_data.txt", "a") as file:
                file.write(f"Name: {value[0]}, Last Name: {value[1]}, Birth Date: {value['-IL-']}\n")
        else:
            pg.popup("Please enter a valid numeric Birth-Date" )
else:
        pg.popup("Please enter your Birth-Date")
Window.close()
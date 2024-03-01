import PySimpleGUI as sg

def read_file(filename):
    try: 
        with open (filename, 'r', encoding='utf8') as file:
            content=file.read()
            return content
        
    except Exception as e:
        return f"error:{e}"
    
def main():
    layout=[
    [sg.Text('Ievadiet txt datnes nosaukumu ar paplašinājumu:')],
    [sg.InputText(key='filename'), sg.FileBrowse()],
    [sg.Button('Nolasīt datni'), sg.Button('Iziet')],
    [sg.Multiline(size=(50, 10), key='output', disabled=True)]
    ]

    window=sg.Window('failu lasītājs', layout)

    while True:
        event, values=window.read()

        if event == sg.WIN_CLOSED or event=='Aizvērt logu':
            break

        if event == "Nolasīt datni":
            filename=values['filename']
            if filename:
                saturs=read_file(filename)
                window['output'].update(saturs)

if __name__=="__main__":
    main()





 
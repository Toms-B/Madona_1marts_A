import PySimpleGUI as sg

import json 
import csv

def read_file(filename):
    try: 
        with open (filename, 'r', encoding='utf8') as file:
            content=file.read()
            return content
        
    except Exception as e:
        return f"error:{e}"
    
def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
    
def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        return data
    


def main():
    layout=[
    [sg.Text('Ievadiet txt datnes nosaukumu:')],
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

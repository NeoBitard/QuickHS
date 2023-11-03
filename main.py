import PySimpleGUI as sg
import hashlib
import os.path

def Hashcodefind(x, HashAlg):
    if os.path.isfile(x) == False:
        return 1
    #if HashAlg == None:
    #    return 2
    f = open(x, 'rb')
    fread = f.read()  
    if HashAlg == 'SHA256':
        Hash = hashlib.sha256(fread)
        return Hash.hexdigest()
    if HashAlg == 'MD5':
        Hash = hashlib.md5(fread)
        return Hash.hexdigest()
    if HashAlg == 'SHA512':
        Hash = hashlib.sha512(fread)
        return Hash.hexdigest()

def AllHashCums(x):
    f = open(x, 'rb')
    fread = f.read()  
    HashSHA256 = hashlib.sha256(fread)
    HashMD5 = hashlib.md5(fread)
    HashSHA512 = hashlib.sha512(fread)
    return 'SHA256: ' + HashSHA256 + '\nMD5: ' + HashMD5 + '\nSHA512: ' + HashSHA512

sg.theme('DarkAmber') 
menu = ['&Edit', ['SHA256', 'MD5', 'SHA512']]

Bmenu = 'SHA256'
l2 = sg.Text('Хешкод файла', size=(15,1)), sg.Input(key='-Shesh-'), sg.Button('Вставить', size=(8,1))
b1 = sg.Text('Файл', size=(15,1)), sg.Input(key='-INPUT-'), sg.FilesBrowse('Поиск', size=(8,1))
l1 = sg.Text('Используется:', size=(15,1)), sg.Text(Bmenu, key='-Understand-', size=(45,1))
b2 = sg.Button('Сравнить',size=(8,1)), sg.ButtonMenu('Хэш-алгоритмы', menu, key='-BMENU-', size=(15,1)), \
    sg.Text('', size=(30,1)), sg.Button('Закрыть', size=(8,1)), sg.FileSaveAs('Экспорт', size=(8,1), key='-EXPORT-', \
    file_types=(('Text', '.txt')), ), 

layout = [ [l2],[b1],[l1],[b2] ]
ll1 = str(l1)


window = sg.Window('QuickHS', layout, icon=r'link.png')

while True:
    event, values = window.read()
    try:
        if values['-BMENU-'] == None:
            values['-BMENU-'] = 'SHA256'
    except:
        pass
    if event == sg.WIN_CLOSED or event == 'Закрыть':
        break
    if event == 'Сравнить':  
        if values['-INPUT-'] != '' and values['-Shesh-']:
            l1Hash = Hashcodefind(values['-INPUT-'], values['-BMENU-'])
            if isinstance(l1Hash, int) == True:
                sg.popup('Ошибка:', l1Hash)
            elif l1Hash == str(values['-Shesh-']):
                sg.popup('Хэш-суммы совпали')
            else:
                sg.popup('Хэш-суммы разные')
        else:
            sg.popup('Одно из полей пустое')
    if event == 'Вставить':
        window['-Shesh-'].update(sg.clipboard_get())
    Bmenu = values['-BMENU-']
    if event == 'Экспорт':
        exportfile = os.path.basename(values['-EXPORT-'])
        #sg.popup(values['-EXPORT-'])
        #f = open(exportfile + '.txt', 'w+')
        #f.write(AllHashCums(values['-INPUT-']))
        #f.close()
    window['-Understand-'].update(values['-BMENU-'])
window.close()


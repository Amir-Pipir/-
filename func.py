from datetime import datetime
from bot import send_convers
import os
from win32com.shell import shell, shellcon
import win32api
import shutil
import random



source_folder = f"C:\\Users\PC\Desktop\{datetime.today().strftime('%d.%m')}"
destination_folder = 'C:\\Users\PC\Desktop\Казань'

def conversion():
    today = datetime.today().strftime('%d.%m')
    kas = int(input("Какая касса?\n"))
    nal = int(input("Сколько нал?\n"))
    peop = int(input("Сколько человек?\n"))
    bm = int(input("Сколько больших магнитов?\n"))
    mm = int(input("Сколько маленьких магнитов?\n"))
    mes = f'\n{today}\n\nНал:{nal}\nБезнал:{kas-nal}\n\nИтого: {kas} руб\n\nКонверсия: {kas // peop} %\n\nБМ: {bm}\n\nММ: {mm}\n\nЧел: {peop}'
    print(mes)
    send_convers(mes)
    
def passive():
    pass


def empty_trash(confirm=True, show_progress=True, sound=True):
    shell.SHEmptyRecycleBin(None, None, 0)


def end():
    empty_trash()
    shutil.move(source_folder, destination_folder)
    os.system("shutdown /s /t 1")


def anecdot():
    x = ["Штирлиц и Мюллер ездили по очереди на танке. Очередь возмущалась, но не расходилась...",
         "Штирлиц приготовился к бою, .... а пришла гёрл...",
         "Штирлиц всю ночь топил камин. На утро камин утонул."]
    print(random.choice(x))



    
    

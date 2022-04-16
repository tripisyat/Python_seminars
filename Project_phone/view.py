# #name = input('Введите фамилию: ')
# def search(name):
#     with open('FIO.txt', 'r', encoding='utf-8') as file: #открываем файл
#         file.readline()
#         for line in file:
#             if name in line:
#                 print(line)

# def from_line_to_dict():
#     fio_dict = dict()
#     with open('FIO.txt', 'r', encoding='utf-8') as file: #открываем файл
#                fio_list=file.read().split('\n') # разбиваем содержимое построчно и получаем список из целых строк

#     for i in  fio_list: # создаем словарь из списка
#         key = i.split()[0] # разбиваем по пробелу и назначаем ключом первый элемент
#         value = i.split()[1:] # остальное разбиваем по пробелу и записываем в значения к ключу
#         fio_dict[key] = value # создаем словарь
#     print(fio_dict)

# from_line_to_dict()



import json
from textwrap import indent
import receive_data as ui



def list_contacts():
    with open("data_base.json", "r") as read_file:
        data = json.load(read_file)
    print(data)

# def add():
#     print("Введите имя контакта:")
#     name = input("> ")
#     print("Введите фамилию контакта:")
#     surname = input("> ")
#     print("Введите отчество контакта:")
#     otchestvo = input("> ")
#     new_contact = {
#         'surname': surname,
#         'name': name,        
#         'otchestvo': otchestvo
#     }
#     with open('FIO.txt', 'a', encoding='utf-8') as file:
#         file.write(ast.literal_eval(new_contact))
    
#     print('Контакт сохранён')
#     return new_contact


import json_generator as jg
import read_file as rf
import add_contact as ac
import del_contact as dc
def hello_user(): 
    print("Добро пожаловать в телефонную книгу.")
    print("""Выберете команду: 
    * list - чтобы посмотреть список контактов.
    * find - найти контакт по имени
    * add  - добавить контакт
    * del  - удаление контакта
    * edit - изменение контакта 
    * exit - выход""")
    choice=input('Введите команду: ')
    # return choice
    # while True:
    #print("\nВведите команду: ")
        # choice = input('> ')
    if choice == 'list':
        rf.read_file()
    # elif choice == 'find':
    #     find(contacts)
    elif choice == 'add':
        ac.write_contact()
    elif choice == 'del':
         dc.delete()
    # elif choice == 'edit': 
    #     edit(contacts)       
    # # elif choice == 'exit':            
    else:
        print("Неизвестная команда")
# def logic(choice):
    
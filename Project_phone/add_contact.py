import receive_data as rd

def write_contact():
    new_contact=rd.add_new()
    with open('FIO.txt', 'a', encoding='utf-8') as file:
        file.write(new_contact)
        file.write(f'\n')
    print('Контакт сохранен')
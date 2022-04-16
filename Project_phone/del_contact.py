import receive_data as rd
def delete():
    del_contact = rd.add_new()
    with open('FIO.txt', 'w+') as file:
        file.replace(del_contact,' ')
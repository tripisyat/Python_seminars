def add_new():
    id = input("Insert new id: ")
    name = input("Insert new name: ")
    surname = input("Insert new surname: ")    
    phone_number = int(input("Insert new phone number: "))
    return str([id, name, surname, phone_number])
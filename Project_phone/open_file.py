import ast

def from_file_to_dict():
    with open('FIO.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    dict = ast.literal_eval(text)
    print (dict)



def rewrite_file(new_data):
    with open('FIO.txt', 'w', encoding='utf-8') as file:
        file.write(new_data)

new_dict = from_file_to_dict()
# rewrite_file(new_dict)
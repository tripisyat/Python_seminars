
def read_file():
    with open('FIO.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        print(text)
#Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
n = 6
index = []
vocabulary = []
for i in range(1, n+1):
    index.append(i)
    vocabulary.append(3*i+i)
print('{', end = '')

for i in range(n):
    print(f'{index[i]}:{vocabulary[i]}', end='')
    if i<n-1:
        print(', ', end="")
print('}')
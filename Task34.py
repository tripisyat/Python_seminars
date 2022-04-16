import random
k = int(input('Введите k '))
list1=[]
for i in range(k):
    y=random.randrange(0,100)
    if y==0:
        continue
    else:
        if i == 0:
            list1.append(f"{y}")
        else:
            list1.append(f"{y}*X**{i}")
list1.append(f"{random.randrange(1,100)}*X**{k}")
print(list1)
data = ""
for i in range(-1,-(k+1), -1):
    if i== -1:
        data =data + list1[i]
    else:
        data =data + " + " + list1[i]
result = f"k={k}=> {data} + {list1[0]} = 0"
print(result)
with open('C:/Users/1/Desktop/python/task_033.txt', 'w') as file:
    file.writelines(result)

a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))

def nod(a,b):
  if a>b:    
    if a%b==0:
      return b
    else:
      while a != b:
        c=a % b
        a=b
        b=c
        return c
  else:
    if b%a==0:
       return a
    else:
       while b != a:
         c=b % a
         b= a
         a=c
         return c        
nod=nod(a,b)

def nok(a, b, nod):
  if a%b==0 or b>a:    
    nok = a*b
  else:
    nok = (a*b)/nod
  return nok
  
print(nok(a, b, nod))
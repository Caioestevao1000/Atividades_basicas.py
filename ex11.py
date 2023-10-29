#Atividade 11
#1b

import os   
import time
os.system('clear')
h = int(input('Digite as horas: '))
m = int(input('Digite os minutos: '))
s = int(input('Digite os segundos: '))
if int(m / 60) != 0:
    h += int(m / 60)
    m = m % 60
if int(s / 60) != 0:
    m += int(s / 60)
    s = s % 60
while(True):
    sh = sm = ss = ''
    if h < 10: sh = '0'
    if m < 10: sm = '0'    
    if s < 10: ss = '0'
    sh += str(h)
    sm += str(m)
    ss += str(s)
    print(f'{sh}:{sm}:{ss}')
    if h <= 0 and m <= 0 and s <= 0:
        break;
    s -= 1
    if s < 0:
        s = 59
        m -= 1
    if m < 0:
        m = 59
        h -= 1
    if h < 0:
        h = 0
    time.sleep(0.1)
    os.system('clear')
print('FIM!')

#1c
n = int(input('Digite um número: '))
for i in range(1,n+1):
    for j in range(i):
        print('*', end='')
    print()

print()
#1d
for i in range(1,n+1):
    print(' '*(n-i), end = '')
    print('* ' * i, end=' ')
    print()
for i in range(2):
    print(' '*(n-1), end = '')
    print('|')
print('Feliz Natal!')
    
#listas
lista = ['Pedro', 'Maria', 'Bispo', 10]
print(lista[2])
#print(lista[4]) erro
print(lista[3])
print(type(lista[2]))
print(type(lista))
print(type(lista[3]))
print(len(lista))
numeros = [5,7,10,-1,50,-12]
print(max(numeros))
print(min(numeros))
print(numeros)
for n in numeros:
    print(n, end= ' ')
print()
lista2 = []
lista2.append('Francisco')
lista2.append('Diego')
print(lista2)
lista2.append('Caio')
lista2.append('Pedro')
print(lista2)
lista2.extend(['Gabryel','Christofer'])
print(lista2)
lista2.remove('Pedro')
print(lista2)
lista2.pop()
print(lista2)
lista2.pop(1)
print(lista2)
#Atividade 10
#1a

for a7 in range(10):
    for a8 in range(10):
        print(f'({a7},{a8})', end=' ')
    print()
print()
#1b
for a6 in range(10, -1, -1):
    print(a6, end=' ')
print()
#1c
for a5 in range(11):
    print(a5*10, end=' ')
print()
#1d
n = int(input('Digite um número: '))
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = ' ')
    print()
print()
#1e
import random
for i in range(10):
    print(random.randrange(0, 101), end = ' ')
    
#atividade 13
#1a
altura = int(input("Digite a altura: "))
largura = int(input("Digite a largura: "))
for i in range(altura):
    for j in range(largura):
        if i == 0 or i == altura-1 or j == 0 or j == largura-1:
            print('*', end='')
        else:
            print('$', end='')
    print()
print()

#exemplos usando time e os
import time
print('Oi')
time.sleep(1)
print('Tchau')
texto = 'Oi, bom dia. Como vai? Eu sou o chat Pedro. '\
+'Provavelmente você não me conhece, mas não'\
+' sei formar frases e nem palavras. Também não sei responder perguntas.'

for letra in texto:
    print(letra, end='', flush = True)
    time.sleep(0.03)
time.sleep(2)
import os   
os.system('clear')
h = 0
m = 0
s = 0
ms = 0
while(True):
    print(f'{h}:{m}:{s}.{ms}')
    ms += 1
    if ms > 9:
        ms = 0
        s += 1
    if s > 59:
        s = 0
        m +=1
    if m > 59:
        m = 0
        h += 1
    time.sleep(0.1)
    os.system('clear')
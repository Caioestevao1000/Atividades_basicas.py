#Atividade 14

#1a
def escrever():
    print('uma frase qualquer')
    
escrever()

#1b
def cumprimentar(nome):
    print(f'Bom dia {nome}!')
    
cumprimentar('Felipe')

#1c
def dobrar(numero):
    print(numero*2)
dobrar(7)

#1d
def somar(n1, n2):
    print(n1 + n2)
somar(22,47)

#1e
def subtrair(n1,n2):
    return n1 - n2
x = subtrair(22,47)
print(x)
print(subtrair(4,3))

#1f
def unir(t1, t2):
    return t1 + t2
texto = unir('Arroz', 'al')
print(texto)

#1g
def is_par(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(is_par(9))

#1g compacto
def is_par2(n): return n % 2 == 0
print(is_par2(int(input('Digite um número: '))))

#primos
#Mostrar na tela somente números primos de 2 a 100;
import math
def is_primo(n):
    for i in range(2,int(n/2)+1):
        if n % i == 0: return False
    return True
def mostrar_primos(inicio, fim):
    for i in range(inicio,fim+1):
        if is_primo(i): print(i, end = ' ')
mostrar_primos(2,100)


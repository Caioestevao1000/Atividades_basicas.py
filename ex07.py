#Atividade 07
#1a

n = int(input("Digite o número da tabuada: "))
i = 0
while i <= 10:
    print(n, "*", i, "=", n*i)
    i += 1

#1b
n = int(input("Digite o número para calcular o fatorial: "))
i = n
s = ''
resp = 1
while i > 0:
    s += str(i)
    if i > 1:
        s += '*'
    resp *= i
    i -= 1
print(s, '=', resp)

#1c
#inicializa uma lista vazia
cores = []
i = 0
while i < 3:
    cor = input('Digite uma cor: ')
    #append adiciona um elemento na lista
    cores.append(cor)
    i += 1
print(cores)

#1d
numeros = []
i = 0
while i < 5:
    n = int(input('Digite um número: '))
    numeros.append(n)
    i += 1
print(numeros)

#Atividade 10
#1a
base = float(input('Digite o valor da base: '))
altura = float(input('Digite o valor da altura: '))
while base <= 0 or altura <= 0:
    print('Valor inválido! Digite novamente')
    base = float(input('Digite o valor da base: '))
    altura = float(input('Digite o valor da altura: '))
area = base * altura
print('A área do retângulo é: ', area)
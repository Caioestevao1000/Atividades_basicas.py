#Atividade 05

#1a

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))
maior = menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('maior: ', maior, 'menor: ', menor)

#Forma mais curta
numeros = input('Digite 3 números separados por vírgula: ').split(',')
maior = menor = int(numeros[0])
if int(numeros[1]) > maior: maior = int(numeros[1])
if int(numeros[2]) > maior: maior = int(numeros[2])
if int(numeros[1]) < menor: menor = int(numeros[1])
if int(numeros[2]) < menor: menor = int(numeros[2])
print('maior: ', maior, 'menor: ', menor)

#1b
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
media = (n1 + n2 + n3)/3 
print('Média: ', media)
if media >= 7:
    print('Aprovado')
else:
    rf = float(input('Digite a nota da recuperação final:'))
    if rf >= 5:
        print('Aprovado em recuperação.')
    else:
        print('Reprovado.')

#1c
numerador = int(input('Digite o numerador:'))
denominador = int(input('Digite o denominador:'))
if denominador == 0:
    print('Não é possível dividir por 0!')
else:
    print(numerador/ denominador)
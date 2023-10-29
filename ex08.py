#Atividade 8
#1b
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número:'))
while n1 < -99 or n1 > 99 or n2 < -99 or n2 > 99:
   print('Valores inválidos. Digite novamente.')
   n1 = int(input('Digite o primeiro número: '))
   n2 = int(input('Digite o segundo número:'))
if n1 > n2:
   maior = n1
   menor = n2
else:
   maior = n2
   menor = n1
print('O maior número é', maior, 'e o menor é', menor)
 
#1c
km = float(input('Digite a distância em km:'))
while km < 0:
   print('Valor inválido. Digite novamente.')
   km = float(input('Digite a distância em km:'))
m = km * 1000
print('A distancia de', km, 'km é equivalente a', m, 'metros')
 
#1d
m = float(input('Digite a distância em m:'))
while m < 0:
   print('Valor inválido. Digite novamente.')
   m = float(input('Digite a distância em m:'))
km = m / 1000
print('A distancia de', m, 'm é equivalente a', km, 'quilometros.')
 
n = int(input('Digite um número inteiro: '))
if n % 3 == 0 and n % 5 == 0:
   print('O número é divisível por 3 e por 5')
else:
   print('O número não é divisível por 3 e por 5')
'''
#1f
usuario = input('Digite seu login:')
senha = input('Digite a sua senha:')
if usuario == 'usuario' and senha == 'senha123':
    print('Acesso concedido!')
else:
    print('Acesso negado!')
 
#varios usuarios
usuarios = ['usuario', 'ygor', 'felipe', 'pedro']
senhas = ['usuario123', 'ygor123456', 'felipe654321', 'pedro123']
#o usuário digitado está na lista de usuarios?
if usuario in usuarios:
    #O usuário está em qual posição na lista?
    indice = usuarios.index(usuario)
    #A senha bate com a senha da lista de senhas na posição do usuário?
    if senha == senhas[indice]:
        print('Acesso concedido!')
    else:
        print('Senha incorreta!')
else:
    print('Usuário inexistente!')


#for
for i in range(5):
    print(i, end=' ')
print()
for i in range(3,9):
    print(i, end=' ')
print()
for i in range(45, 89, 2):
    print(i, end=' ')
print()
for i in range(20,9,-1):
    print(i, end=' ')
print()
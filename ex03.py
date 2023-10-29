'''
Atividade 03
 
'''
#1a
 
     #converter string para inteiro
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('tipo do n1',type(n1))
print('tipo do n2',type(n2))
res = n1 + n2
print(res)
 
#1b
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('tipo do n1',type(n1))
print('tipo do n2',type(n2))
res = n1 * n2
print(res)
 
#----- converter float para int
n1 = 2.45
print('tipo do n1',type(n1))
n1 = int(n1)
print('valor:',n1, 'tipo do n1',type(n1))
#----- converter int para float
n1 = 4
print('valor:',n1, 'tipo do n1',type(n1))
n1 = float(n1)
print('valor:',n1, 'tipo do n1',type(n1))
 
#1c
n1 = int(input('Digite um número: '))
print(n1**2);
 
#1d
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
media = (n1 + n2)/2
print('A nota do aluno foi: ', media)
#-----
n1 = 2 + 3 * 5 / 2 - 1
print(n1)

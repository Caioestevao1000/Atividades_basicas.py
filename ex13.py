#Atividade 13
#1a

meses = ('jan','fev','mar','abr','mai','jun','jul'\
,'ago','set','out','nov','dez')
print(meses[8])
#1b
computador={
    'Processador':'Core i7',
    'Armazenamento':'500gb SSD',
    'Memória': '32GB',
    'Placa-mãe':'Asus'
}
print(computador)
print(computador['Processador'])
for chave in computador:
    print(f'{chave}:{computador[chave]}')
#1c
conceitos = {'if','elif','else','while','for'}
print(conceitos)
for item in conceitos:
    print(item, end = ' ')
print()
#1d
pessoa1 = {
    'nome':'Ygor',
    'cpf':'123456',
    'telefone':'(43)99999-999',
    'endereco':'R. Belem'
}
#1e
pessoa2 = {
    'nome':'Christofer',
    'cpf':'122223445386',
    'telefone':'(43)9998-9999',
    'endereco':'Rua S. Vicente'
}
lista = [pessoa1, pessoa2]
print(lista)
for pessoa in lista:
    for dado in pessoa:
        print(f'{dado}: {pessoa[dado]}')
    print('--------------')
print()

#1e diferente
lista = [{
    'nome':'Ygor',
    'cpf':'123456',
    'telefone':'(43)99999-999',
    'endereco':'R. Belem'
},
{
    'nome':'Christofer',
    'cpf':'122223445386',
    'telefone':'(43)9998-9999',
    'endereco':'Rua S. Vicente'
}]
for pessoa in lista:
    for dado in pessoa:
        print(f'{dado}: {pessoa[dado]}')
    print('--------------')
print()
#1f
comando = 0
while True:
    chave_busca = ''
    comando = int(input('''
1 - Buscar por nome
2 - Buscar por cpf
3 - Buscar por telefone
4 - Buscar por endereço
9 - Sair
    '''))
    if comando == 9: break
    elif comando == 1: chave_busca = 'nome'
    elif comando == 2: chave_busca = 'cpf'
    elif comando == 3: chave_busca = 'telefone'
    elif comando == 4: chave_busca = 'endereco'
    else: 
        print('Comando inválido!')
        continue
    termo_busca = input('Digite o termo de busca: ')
    for pessoa in lista:
        if chave_busca in pessoa and pessoa[chave_busca] == termo_busca:
            for dado in pessoa:
                print(f'{dado}: {pessoa[dado]}')
            print('--------------')
    print()
print('FIM')

#1g
pessoa1 = {'Python', 'Java', 'C++', 'C#', 'SQL'}
pessoa2 = {'Python', 'Java', 'C++', 'Assembly', 'HTML'}
uniao = pessoa1.union(pessoa2)
print('União: ')
for item in uniao: print(item, end = ' ')
print()
interseccao = pessoa1.intersection(pessoa2)
print('Intersecção')
for item in interseccao: print(item, end = ' ')
print()

#FUNÇÕES
def cumprimentar():
    print('Bom dia :)')

def cumprimentar_nome(nome):
    print('Bom dia', nome)
    
def somar(n1:int, n2:int):
    print(n1+n2)

def subtrair(n1, n2):
    return n1 - n2
    
cumprimentar()
cumprimentar()
cumprimentar()
cumprimentar_nome('Maria')
somar(3.5,4)
somar(4,5)
numero = subtrair(10,2)
print(numero)
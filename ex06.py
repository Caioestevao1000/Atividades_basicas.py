#atividade 06
#1a

apitos = int(input("Digite o número de apitos: "))
if apitos == 1: print('Atualização de DRAM')
elif apitos == 2: print('Circuito de Paridade')
elif apitos == 3: print('Memória Base 64K RAM')
elif apitos == 4: print('Timer do Sistema')
elif apitos == 5: print('Processador')
else: print('Número inválido.')

#1b
'''
nota >= 9,0 -> Excelente
>= 7,0 e < 9,0 -> Bom
>= 5,0 e < 7,0 -> Razoável
< 5,0 -> Fraco

código fraco

nota = int(input('Digite a nota do aluno: '))
if nota >= 9.0: print('Excelente')
elif nota >= 7: print('Bom')
elif nota >= 5: print('Razoável')
else: print('Fraco')

código melhor
'''
nota = int(input('Digite a nota do aluno: '))
if nota >= 9.0 and nota <= 10: print('Excelente')
elif nota >= 7 and nota < 9: print('Bom')
elif nota >= 5 and nota < 7: print('Razoável')
elif nota < 5:print('Fraco')
else: print('Nota inválida!')

#1c
hora = int(input('Digite a HORA do dia:'))
if hora >= 0 and hora < 6: print('Boa madrugada')
elif hora >= 6 and hora < 12: print('Bom dia')
elif hora >= 12 and hora < 18: print('Boa tarde')
elif hora >= 18 and hora <= 23: print('Boa noite')
else: print('Hora inválida.')


i = 0
while i < 5:
    print(i, 'Maria')
    i += 1
    
while True:
    nota = float(input('Digite nota: '))
    if nota < 0 or nota > 10:
        print('Nota invalida!')
    else:
        break
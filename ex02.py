"""
Comentário de bloco
ou seja
pode ocupar várias linhas
"""
nome = input('Qual é o seu nome? ')
print('Oi', nome, '!!!')
sentimento = input('Como você se sente hoje? ')
if sentimento == 'Bem':
    print('Que bom!')
elif sentimento == 'Dolorido':
    print('Recomendo que visite um médico especialista.')
elif sentimento == 'Mal':
    print('Que pena!')
else:
    print('Nossa!')
    
altura = input('Qual é a sua altura em centimetros? ')
print(type(altura))
altura_cm = int(altura)
print(type(altura_cm))
if altura_cm < 170:
    print('Você tem a estatura menor que a média!')
elif altura_cm < 180:
    print('Você tem uma estatura média.')
else: 
    print('Você tem uma estatura acima da média!')
    
almoco = input('Você já almoçou hoje? ')
print(type(almoco))
if 'sim' in almoco: 
    print('Ah então tá.')
    if 'bom' in almoco:
        print('Eu também gostei.')
    if 'faltou' in almoco:
        print('Mas é melhor do que não ter nada.')
else:
    almoco2 = input('Bora almoçar? ')
    if 'sim' in almoco2 or 'partiu' in almoco2 \
        or 'bora' in almoco2 or 'vamo' in almoco2:
        print('Partiu, vai rolar coquinha?')
    else: 
        print('Então tá bom então.')
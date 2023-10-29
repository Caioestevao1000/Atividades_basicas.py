#Atividade 12

lista = [1,2,3,4]
lista[2] = 20
print(lista[2])
print(lista)
tupla = ("Christofer", "Felipe", "Caio")
print(tupla)
print(tupla[1])
#tupla[1] = 'Gabryel' erro
figado = {'Christofer', 'Felipe'}
coco = set(['Diego', 'Pedro','Francisco', 'Luis', 'Gabryel', 'Christofer'])
print('figado', figado)
print('coco', coco)
#print(coco[2]) erro
print(figado.union(coco))
print(coco.intersection(figado))
uva = {'Pedro', 'Gabryel'}
print(coco.issuperset(uva))
print(coco.issuperset(figado))
print(uva.issubset(coco))
print(figado.issubset(coco))
uva.add('Caio')
print(uva.issubset(coco))
uva.remove('Caio')
print(uva.issubset(coco))
luis = {
    'nome':'Luis',
    'cpf': '123456678',
    'idade': 18,
    'hobbies':['desenhar','jogar']
}
maria = {
    'nome': 'Maria',
    'cpf':'foi hackeada',
    'idade':17,
    'hobbies':['jogar','programar']
}
print(luis)
print(maria)
sala = {
    'nome': 'Turma de Redes',
    'horario': 'Vespertino',
    'alunos': [luis, maria]
}
print(sala)
print(sala['nome'])
print(luis['hobbies'])
sala['horario'] = 'Matutino'
print(sala['horario'])

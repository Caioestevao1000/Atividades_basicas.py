#Atividade 04 1a
 
horas_semana = int(input("Digite a quantidade de horas trabalhadas: "))
salario_hora = float(input("Digite a valor do salario por hora: "))
salario_semanal = horas_semana * salario_hora
print("O valor do salário semanal do funcionário é R$ ", salario_semanal)
 
#1b
salario_mensal = salario_semanal * 4
print("O valor do salário mensal do funcionário é R$ ", salario_mensal)
 
 
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
 
#tanto o comando elif e else só podem existir em conjunto com o if
#if n1 > n2:
#    diferenca = n1 - n2
#else:
#    diferenca = n2 - n1
 
#outra forma de resolver
diferenca = n1 - n2
if diferenca < 0:
    diferenca = diferenca * -1
 
print("A diferença é de: ", diferenca)
 
 
#1c
dist = float(input("Digite  a distância percorrida: "))
litros = float(input("Digite a quantidade abastecida: "))
eficiencia = dist / litros
print("A eficiência do veículo é de", eficiencia,"km/l")
 
#1d
ef_gasolina = float(input("Digite a eficiência com gasolina: "))
ef_etanol = float(input("Digite a eficiência com etanol: "))
preco_gasolina = float(input("Digite o preço do litro da gasolina: "))
preco_etanol = float(input("Digite o preço do litro do etanol: "))
valor_km_gasolina = preco_gasolina/ef_gasolina
valor_km_etanol = preco_etanol/ef_etanol
print("O valor do km com gasolina é de R$", valor_km_gasolina)
print("O valor do km com etanol é de R$", valor_km_etanol)
 
#if elif e else
n1 = int(input("Digite um número: "))
 
if n1 == 0:
    print("n1 é igual a 0")
elif n1 < 10:
    print("n1 é menor que 10")
elif n1 < 20:
    print("n1 é menor que 20")
else:
    print("n1 é maior ou igual a 20")
 
#Atividade 05 1a
nota = float(input("Digite a nota: "))
if nota < 0 or nota > 10:
    print("Nota inválida!")
else:
    print("Nota válida! ", nota)
 
#1b
num = int(input("Digite um número: "))
if num%2 == 0:
    print("O número", num, "é par!")
else:
    print("O número", num, "é ímpar!")
   
 
#1d
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
if num1 > num2:
    print(num1+num2)
else:
    print(num1*num2)
 
#1c
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
operacao = input("Digite a operação (+, -, *, /)")
if '+' in operacao:
    print(num1 + num2)
elif '-' in operacao:
    print(num1 - num2)
elif '*' in operacao:
    print(num1 * num2)
elif '/' in operacao:
    print(num1 / num2)
 
#calculadora HP da maria
#expressao = input("Digite a expressão: ")
#print(eval(expressao))
 
print(eval(input("Digite a expressão: ")))

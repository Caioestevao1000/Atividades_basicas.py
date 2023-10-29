#atividade 9
#1a e 2a
a1 = 0
while a1 < 5:
    print(a1, end = " ")
    a1 += 1
print()
for a1 in range(5):
    print(a1, end = " ")
print()
#1b e 2b
a2 = 0
while a2 < 3:
    print(a2*10, end = " ")
    a2 += 1
print()
for a2 in range(3):
    print(a2*10, end = " ")
print()
#1c e 2c
a3 = 20
while a3 > 10:
    print(a3, end = " ")
    a3 -= 1
print()
for a3 in range(20,10,-1):
    print(a3, end = " ")
print()
#1d e 2d
a4 = 0
while a4 < 10:
    print(a4, end = " ")
    a4 += 1
print()
for a4 in range(10):
    print(a4, end = " ")
print()
#outro for, com range tendo 2 parâmetros
for i in range(3,9):
    print(i, end = ' ')
print()
#for aninhado
for i in range(5):
    for j in range(10):
        print('.', end=' ')
    print()
print()
for i in range(3):
    for j in range(4):
        for k in range(5):
            print ('(',i,j,k,')', end = ' ')
        print('-------')
    print('=======')

print()
for i in range(4):
    for j in range(10):
        print('(',i,j,')', end=' ')
    print()
print()
#cartelinha
for i in range(6):
    for j in range(1,11):
        n = i*10 + j 
        s = ''
        if n < 10:
            s += '0'
        s += str(n)
        print('[ ',s, ' ]', end = ' ')
    print()
print()

#cartelinha2
for i in range(10):
    for j in range(10):
        n = i*10 + j 
        s = ''
        if n < 10:
            s += '0'
        s += str(n)
        print('[ ',s, ' ]', end = ' ')
    print()
print()

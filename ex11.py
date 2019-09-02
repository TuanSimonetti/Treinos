n1 = float(input('Qual sua nota na prova 1: '))
n2 = float(input('Qual sua nota na prova 2: '))
m = (n1 + n2)/2

print('A sua média foi {:.2f}'.format(m))
print('Parabéns!' if m >=7 else 'Estude mais!')

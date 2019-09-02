import random
velocidade = random.randint(0, 150)

if velocidade >= 80:
    print('Você excedeu o limite de velocidade, sendo multado em {} reais.'.format((velocidade - 80)*7))
else:
    print('Você está seguindo regularmente o limite de velocidade.')
print('')

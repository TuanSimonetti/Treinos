import random
num = random.randint(0, 10)

num2 = int(input('Por favor, diga-me um número de 0 à 10 e veremos se esse número é sorteado: '))
if num2 == num:
    print('Parabéns, você acertou!')
else:
    print('Infelizmente, você não acertou. Mais sorte na próxima vez.')
print('')

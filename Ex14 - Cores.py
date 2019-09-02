#\033[style; text; back]
#ou seja: stylo; cor do texto; cor do fundo

#\033[033:44m

#Style: 0, 1, 4 e 7:
# 0 - Nada, sem estilo;
# 1 - Negrito;
# 4 - Sublinhado
# 7 - Inversão da cor da letra com a do fundo

#Text: 30, 31, 32, 33, 34, 35, 36, 37:
# 30 - Branco
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul
# 35 - Roxo
# 36 - Azul claro
# 37 - Cinza
# Para acrescentar mais cores, precisa importar uma biblioteca

# Back: 40, 41, 42, 43, 44, 45, 46, 47:
# 40 - Funco Branco
# 41 - Funco Vermelho
# 42 - Fundo Verde
# 43 - Funco Amarelo
# 44 - Fundo Azul
# 45 - Fundo Roxo
# 46 - Fundo Azul claro
# 47 - Fundo Cinza

#\033[0; 30; 41m
#\033[4; 33; 44m
#\033[0; 35; 43m
#\033[30; 42m
#\033[m
#\033[7; 30m

print('\033[4;30;45mOlá, mundo!\033[m')
print('\033[0;34;43mOlá, mundo!\033[m')
print('\033[1;36;47mOlá, mundo!\033[m')
print('\033[0;34;40mOlá, mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{} e \033[31m{}'.format(a, b))

nome = 'Simonetti'
print('Olá! Muito prazer em te conhecer, {}{}{}'.format('\033[4;32m', nome, '\033[m'))

cores = {'Limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebanco':'\033[7;30m'}

print('Olá, mundo, {}{}{}!'.format(cores['Limpa'], nome, cores['azul']))

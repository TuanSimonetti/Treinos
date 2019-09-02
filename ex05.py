import random
n1 = str(input('Aluno a: '))
n2 = str(input('Aluno b: '))
n3 = str(input('Aluno c: '))
n4 = str(input('Aluno d: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("A ordem dos alunos será: ")
print(lista)

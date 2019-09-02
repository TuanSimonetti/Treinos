class Data:
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(d1)

d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020
print(d2)



class Numero:
    def __int__(self):
        return f'{self.primeiro}, {self.segundo} e {self.terceiro}'


n1 = Numero()
n1.primeiro = int(input("Me fale um número: "))
n1.segundo = int(input("Me fale outro número: "))
n1.terceiro = int(input("Me fale o ultimo número: "))
print(n1)


class colocação:
    def __str__(self):
        return f'{self.primeiro}; {self.segundo}; {self.terceiro}'


c = colocação()
c.primeiro = input("Me fale o primeiro à chegar: ")
c.segundo = input("Me fale o segundo à chegar: ")
c.terceiro = input("Me fale o terceiro à chegar: ")
print(c)

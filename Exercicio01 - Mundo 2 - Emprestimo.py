cliente = str(input('Olá, eu sou Simonetti, seu gerente virtual. Por gentileza, qual seu nome?'))
vcasa = float(input('{}, é um enorme prazer poder te conhecer e lhe atender. Por gentileza, a fim de iniciarmos os procedimentos, você me informa o valor do imóvel que deseja adquirir?'.format(cliente)))
salario = float(input(' Maravilha, {}. O valor do imóvel é R$ {}. E qual o valor de sua renda mensal? '.format(cliente, vcasa)))
prazo = int(input('Jóia. Em quantas parcelas você deseja realizar o pagamento? '))
limite = (salario*30)/100
parcela = (vcasa / prazo)
if parcela >= limite:
    print('{}, infelizmente, não poderemos aprovar o financiamento nessas condições.'.format(cliente))
else:
    print('{}, seu emprestimo pode ser aprovado.'.format(cliente))
print('='*30)

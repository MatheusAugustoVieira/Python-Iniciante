salário = float(input('Qual o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R$\033[1;31m{:.2f}\033[m passa a ganhar R$\033[1;32m{:.2f}\033[m agora'.format(salário, novo))


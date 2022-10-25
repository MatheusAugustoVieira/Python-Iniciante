num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
um = num // 10000 % 10
dm = num // 100000 % 10
cm = num // 1000000 % 10

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
print('Unidade de Milhar: {}'.format(um))
print('Dezena de Milhar: {}'.format(dm))
print('Centena de Milhar: {}' .format(cm))


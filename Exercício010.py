real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dólar = real / 5.78
euro = real / 6.80
print('Com R${} você pode comprar US${:.2f} e {:.2f}'.format(real, dólar, euro))

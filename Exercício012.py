preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 17 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 17% vai custar R${:.2f}'.format(preço, novo))

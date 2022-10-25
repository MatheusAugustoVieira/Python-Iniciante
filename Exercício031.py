distância = float(input('\033[1;32mQual a distância da sua viagem?\033[m '))
print('Você está prestes a começar uma viagem de \033[36m{}Km\033[m'.format(distância))
'''if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45'''
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço de sua passagem será de R$\033[31m{:.2f}\033[m'.format(preço))
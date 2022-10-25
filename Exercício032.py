ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} \033[1;32mÉ BISSEXTO\033[m'.format(ano))
else:
    print('O ano {} \033[1;31mNÃO É BISSEXTO\033[m'.format(ano))

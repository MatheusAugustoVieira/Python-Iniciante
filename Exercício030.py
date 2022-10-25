número = int(input('\033[35mMe diga um número qualquer:\033[m'))
resultado = número % 2
if resultado == 0:
    print('O número {} é \033[34mPAR\033[m'.format(número))
else:
    print('O número {} é \033[31mÍMPAR\033[m'.format(número))



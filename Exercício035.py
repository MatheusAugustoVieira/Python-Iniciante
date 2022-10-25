print('\033[1;32m-=-\033[m'*9)
print('\033[1;34mAnalisador de Triângulos\033[m')
print('\033[1;32m-=-\033[m'*9)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m triângulo!')
else:
    print('O segmentos acima \033[1;31mNÃO PODEM FORMAR\033[m triângulo!')




n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1+n2

print('\033[1;31m-=-\033[m'*10)
print('A soma entre \033[1;35m{}\033[m e \033[1;36m{}\033[m vale \033[1;32m{}\033[m'.format(n1, n2, s))
print('\033[1;31m-=-\033[m'*10)


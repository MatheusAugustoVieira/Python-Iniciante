from random import randint
from time import sleep
from termcolor import colored
import playsound
computador = randint(0, 1) #Faz o computador "PENSAR"
print(colored('-=-', 'yellow')*20)
print(colored('Vou pensar em um número entre 0 e 1. Tente adivinhar...', 'blue'))
print(colored('-=-', 'yellow')*20)
jogador = int(input('Em que número eu pensei?')) #Jogador tenta Adivinhar
print(colored('PROCESSANDO...', 'magenta'))
sleep(2)
if jogador == computador:
    print(colored('PARABÉNS! Você conseguiu me vencer!', 'green'))
    playsound.playsound('acertou.mp3')
else:
    print(colored('GANHEI! Eu pensei no número {} e não no {}', 'red').format(computador, jogador))
    playsound.playsound('Errou.mp3')

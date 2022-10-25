from termcolor import colored
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print(colored('MULTADO! Você excedeu o limite permitido que é 80Km/h', 'red'))
    multa = (velocidade - 80) * 7
    print(colored('Você deve pagar uma multa de R${:.2f}', 'red').format(multa))
print(colored('Tenha um bom dia! Dirija com segurança!', 'green'))

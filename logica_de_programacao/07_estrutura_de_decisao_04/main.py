'''
Programa que irá receber do usuário dois números reias  e 
o usuário irá escolher uma  das quatro operações básicas da matemática, 
e o programa irá calcular com base na escolha do usuário e infromar o resultado
'''
#TODO
#variáveis
n1= float(input('Digite o primeiro número: ').replace(',','.'))
n2= float(input('Ditie o segundo número: ').replace(',','.'))
#menu
print(f'{'-'*20}CALCULADORA PYTHON {'-'*20}')
print('1 = Soma')
print('2 = Subtração')
print('3 = Multiplicação')
print('4 = Divisão')
operador = input('Escolha o operador : ')
# verifica a operação escolhida e faz o cálculo
match operador:
    case '1':
        print(f'O resultado da some é: {n1+n2:.2f}')
    case '2':
        print(f'O resultado da subtração é: {n1-n2:.2f}')
    case '3':
        print(f'O resultado da multiplicação é: {n1*n2:.2f}')
    case '4':
        print(f'O resultado da divisão é: {n1/n2:.2f}')
    case _:
        print(f'Operador inválido. ')
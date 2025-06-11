'''crie um programa que receba o nome do usuário e a idade,
e informe o menu abaixo:
SALA 1 - A roda quadrada -Livre
SALA 2 - A volta dos que não foram
SALA 3 - Poeira em Alto mar 
SALA 4 - As tranças do Rei Careca - 16 anos
SALA 5 - A vingança do farngo assado - 18 anos
o usuário deverá escolher a sala do filme que deseja assistir,
e o programa deverá:
-Liberar a entrada do usuário e encerrar, caso o usuário tenha a idade mínima, ou maior 
-Bloquear a entrada do usuário e pedir para o mesmo escolher outro filme,
caso não tenha a idade mínima
''' 
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
while True:
    print('-'*55)
    print('Filmes disponíveis:\n Sala 1 - A Roda Quebrada - Livre\nSala 2 - A volta dos Que Não Foram - 12 anos\nSala 3 - Poeira em Alto MAR - 14 ANOS\nSala 4 - As Traças do Rei Careca - 16 anos\nSala 5 - A Vingança do Frango Assado - 18 anos')
    sala = input('Digite qual a sala de filme escolhida: ')
    print('-'*55) 
    match sala:
        case '1':
            print('Entrada liberada tenha um execelente filme')
            break
        case '2':
            if idade >= 12:
                print('Entrada liberada tenha um execelente filme')
                break
            else:
                print('Entrada proibida! Sua idade é abaixo da indição do filme') 
                continue
        case '3':
            if idade >= 14:
                print('Entrada liberada tenha um execelente filme')
                break
            else:
                print('Entrada proibida! Sua idade é abaixo da indição do filme')
                continue
        case '4':
            if idade >= 16:
                print('Entrada liberada tenha um execelente filme')
                break
            else:
                print('Entrada proibida! Sua idade é abaixo da indição do filme')
                continue
        case '5':
            if idade >= 18:
                print('Entrada liberada tenha um execelente filme')
                break
            else:
                print('Entrada proibida! Sua idade é abaixo da indição do filme')
                continue
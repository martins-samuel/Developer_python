while True:
    # confere o n1
    while True:
        try:
            n1 = float(input('Digite o primeiro número real: ').replace(',', '.'))
            break
        except ValueError:
            print('Valor inválido! Por favor, insira um número real.')

    # confere n2
    while True:
        try:
            n2 = float(input('Digite o segundo número real: ').replace(',', '.'))
            break
        except ValueError:
            print('Valor inválido! Por favor, insira um número real.')

    # confere 
    while True:
        print('\nEscolha uma das operações abaixo:')
        print('Sair do Program = "0"\nSOMA = "1"\nSUBTRAÇÃO = "2"\nMULTIPLICAÇÃO = "3"\nDIVISÃO = "4"')
        print('-' * 20)
        operador = input('Digite um operador: ').strip()
        if operador in ('0','1', '2', '3', '4'):
            break
        else:
            print('Operador inválido! Tente novamente com uma opção de 1 a 4.')

    # calcula
    match operador:
        case '0':
            print('Programa encerrado')
            break
        case '1':
            print(f'Os números {n1} e {n2} somados dão {n1 + n2}')
        case '2':
            print(f'Os números {n1} e {n2} subtraídos dão {n1 - n2}')
        case '3':
            print(f'Os números {n1} e {n2} multiplicados dão {n1 * n2}')
        case '4':
            if n2 == 0:
                print('Não existe divisão por ZERO')
            else:
                print(f'Os números {n1} e {n2} divididos dão {n1 / n2}')

    # da opçao de começar denovo
    continuar = input('\nDeseja fazer outro cálculo? (s/n): ').strip().lower()
    if continuar != 's':
        print('Programa encerrado!')
        break 
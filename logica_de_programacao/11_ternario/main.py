try:
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade : '))

    result = 'É maior de idade.' if idade >= 18 else 'é menor de idade'
    print(f' {nome } sa{result}')
finally:
    print('Programa encerrado')
#tratamento de exceção
try:
    numero =int(input('Digite um número inteiro: '))
    # laço de repetição
    while numero >= 0:
        print(numero)
        numero -= 1
except Exception as e:
    print(f'Não foi possível fazer a contagem {e}')
finally:
    print('Programa encerrado! ')
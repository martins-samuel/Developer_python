import os
import equacoes as eq
def menu():
    print('1 - Deseja calcular uma equação de 1° Grau')
    print('2 - Deseja calcular uma equação de 2° Grau')
    print('3 - Encerrar o programa ')

if __name__ == '__main__':
    while True:
        menu()
        try:
            opcao = int(input('Digite a operação escolhida:  '))
            os.system('cls' if os.name == 'nt' else 'clear')
            match opcao:
                case 1:
                    a = float(input('Infrome o valor de A: ').replace(',','.'))
                    b = float(input('Infrome o valor de B: ').replace(',','.'))
                    os.system('cls' if os.name == 'nt' else 'clear')
                    result = eq.equacao_1o_grau(a,b)
                    print(f'{a}X +{b} = 0' if b >= 0 else f"{a}X{b} = 0")
                    print(f'X = {result}')
                    continue
                case 2:
                    a = float(input('Infrome o valor de A: ').replace(',','.'))
                    b = float(input('Infrome o valor de B: ').replace(',','.'))
                    c = float(input('Infrome o valor de C: ').replace(',','.'))
                    os.system('cls' if os.name == 'nt' else 'clear')
                    result = eq.equacao_2o_grau(a,b,c)
                    for x in result:
                        print(x)
                    continue
                case 3:
                    print('Programa encerrado')
                    break
                case _:
                    print('Operação inválida')
                    continue
        except Exception as e:
            print(f'Entrada inválida digite uma opção válida {e} ')
            continue

"""# TODO - atividade: Crie um programa onde o usuário possa fazer as seguintes operações:
- Calcular área de um quadrado
- Calcular área de um retângulo
- Calcular área de um triângulo
- Calcular área de um trapézio
- Sair do programa
# NOTE - o usuário deverá escolher a operação em um menu
# NOTE - o programa deverá ser feito com funções
"""
import os
def menu_escolha():
    print('Digite a sua operação escolhida: ')
    print('1 = Calcular área de um quadrado ')
    print('2 = Calcular área de um retângulo ')
    print('3 = Calcular área de um triângulo ')
    print('4 = Calcular área de um trapézio ')
    print('5 = Sair do programa ')
    
def area_quadrado():
    lado = float(input('Digite o lado do quadrado: ').replace(',','.'))
    area = lado ** 2
    print(f"A área do quadrado é {area:.2f}\n")
    
def area_retangulo():
    base = float(input('Digite a base do seu retângulo: ').replace(',','.'))
    altura = float(input('Digite a altura do seu retângulo: ').replace(',','.'))
    area = base * altura
    print(f"A área do retângulo é {area:.2f}\n")
    
def area_triangulo():
    base = float(input('Digite a base do seu triângulo: ').replace(',','.'))
    altura = float(input('Digite a altura do seu triângulo: ').replace(',','.'))
    area = (base * altura)/2
    print(f"A área do triângulo é {area:.2f}\n")
    
def area_trapezio():
    base_maior = float(input('Digite a base  maior do seu trapézio: ').replace(',','.'))
    base_menor = float(input('Digite a base  menor do seu trapézio: ').replace(',','.'))
    altura = float(input('Digite a altura do seu trapézio: ').replace(',','.'))
    area = (base_maior + base_menor) * altura / 2
    print(f"A área do trapézio é {area:.2f}\n")
    
def main():
    while True:
        menu_escolha()
        try:
            escolha = int(input('Digite a operação escolhida:  '))
            os.system('cls')
        except Exception as e:
            print(f'Entrada inválida digite uma opção válida {e} ')
            continue
        
        
        match escolha:
            case 1:
                area_quadrado()
            case 2:
                area_retangulo()
            case 3:
                area_triangulo()
            case 4:
                area_trapezio()
            case 5:
                print('Programa encerrado')
                break
            case _:
                print("Opção inválida. Tente novamente.\n")
                
main()

'''
Crie um programa que calcule a euqação do 1°  grau 
# NOTE - Coloque um menu para o usuário decidir se quer calcular a equação ou sair do programa
# NOTE - Coloque no menu a opção de calcular a euqação do 2° grau (não precisa )'''
import math
def equacao_1o_grau(a,b):
    x = -b/a 
    return x
def equacao_2o_grau(a,b,c):
# a * X² + b * X + c = 0
    delta = (b ** 2) -(4*a*c)
    if delta > 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        yield f"x' = {x1}"
        yield f'x" = {x2}'
    elif delta == 0:
        x = -b/(2*a)
    else:
        yield f'Não há raízes reais'
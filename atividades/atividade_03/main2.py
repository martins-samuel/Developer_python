'''
Crie um programa que receba o nome, o peso 
e a altura do usuário, e informe seu IMC (Índice de Massa Corporal)
r informe seu diagnóstico de acordo com o valor de seu IMC
-MAGRO demais
-Peso normal
-Acima do peso
-Obeso
-Obesidade nivel II
-Obesidade nível III
'''
#Entrada das variáveis
nome = input('Digite o seu nome: ')
while True:
    try:
        peso = float(input('Digite o seu peso: ').replace(',','.'))
        break
    except ValueError:
        print('Escreva um valor válido ')
while True:
    try:
        altura = float(input('Digite a sua altura em metros: ').replace(',','.'))
        break
    except ValueError:
        print('Escreva um valor válido')
imc = peso/ (altura ** 2)
if imc >= 18.5 and imc <= 24.9:
    print(f'Seu imc ésta na faixa da magreza imc = {imc:.2f}')
elif imc >= 25 and imc <= 29.9:
    print(f'Seu imc está na faixa do peso normal imc = {imc:.2f}')
elif imc >= 30 and imc <= 34.9:
    print(f'Seu imc está na faixa de sobrepeso imc = {imc:.2f}')
elif imc >= 35 and imc <= 39.9:
    print(f'Seu imc está na faixa de obesidade grau I imc = {imc:.2f}')
else:
    print(f'Seu imc está na faixa de obesidade grau II imc = {imc:.2f}') 

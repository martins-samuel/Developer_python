nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade : '))
altura = float(input('Digite a sua altura em metros: ').replace(',','.'))
if idade >= 12 and altura >= 1.1:    
    print(f'Você, {nome} está habito para ir no brinquedo pois tem {idade} é  de {altura:.2f} M')
else: 
    print('Você não tem as condições necessárias suficiente')
nome = input('Digite o seu nome: ')
media = float(input('Qual é a sua média: ').replace(',','.'))
if media > 0 and media <= 10:
    if media >= 7:
        print(f'Você, {nome} está aprovado pois sua média foi {media}')
    elif media < 7 and media >= 5:
        print(f' Você, {nome} está de Recuperação pois sua média foi {media}')
    else: 
        print(f'Você, {nome} está Reprovado pois sua média foi {media}')
else:
    print('Média inválida')
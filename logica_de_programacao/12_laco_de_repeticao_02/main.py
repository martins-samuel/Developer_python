
#laço de repetição 
while True:
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade : '))
    result = 'é maior de idade' if idade >= 18 else 'é menor de idade'
    print(f' {nome} {result}')
    repetir = input('Deseja verificar de novo? (s/n)').lower().strip()
    match repetir:
        case 's':
            continue
        case 'n':
            break
        case _:
            print('Opção inválida')

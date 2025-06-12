import os 

#lista 
nomes = [
    'Fulano',
    'Ciclano',
    'Beltrano',
    'João',
    'Maria',
    'José',
    'Alex',
    'Fernanda',
    'Alexa',
    'Alexandra',
    'Joana'
]
# exibe a lista original
for i in range(len(nomes)):
    print(f'Índice {i}: {nomes[i]}.')
# usuário informa a posição da lista que deseja excluir
try:
    i = int(input('Informe a posição que deseja excluir: '))
    os.system('cls')
    if i >= 0 and i < len(nomes):
        print(f'Item a ser excluído: {nomes[i]}')
        confirma = input(f'Deseja excluir {nomes[i]}? (s/n)').lower().strip()
        os.system('cls')
        match confirma:
            case 's':
                item_excluidos = nomes[i]
                del(nomes[i])
                print(f'Item {item_excluidos} excluído com sucesso ')
            case 'n':
                print(f'{nomes[i] } não será excluído')
            case _:
                print('Opção inválida')
except Exception as e:
    print(f'Não foi possível excluir item. {e}')
finally:
    print(f'Nova Lista:\n')
    for i in range (len(nomes)):
        print(f'Índice {i}: {nomes[i]}.')

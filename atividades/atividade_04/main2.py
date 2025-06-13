
'''
Crie um programa em que o usuário pode escolher entre:
-Inserir um nome em uma lista
-Exibir a lista de nomes
-Pesquisar por um nome na lista
-Alterar item na lista
-Excluir item da lista
-Sair do programa
"""
# NOTE - a lista deve começar vazia.
# NOTE - todos os nomes devem ser inseridos pelo usuário.
# NOTE - DIVIRTAM-SE!!! =D'''
import os

nomes = []

while True:
    try:
        print('-' * 55)
        print('1 - Inserir um nome na lista')
        print('2 - Exibir a lista de nomes')
        print('3 - Pesquisar um nome na lista')
        print('4 - Alterar algum nome na lista')
        print('5 - Excluir algum nome da lista')
        print('6 - Sair do programa')
        print('-' * 55)

        entrada = int(input('Digite a opção escolhida: '))
        os.system('cls')

        match entrada:
            case 1:
                nome_novo = input('Digite um novo nome na lista: ').strip().capitalize()
                nomes.append(nome_novo)
            case 2:
                if not nomes:
                    print('A lista está vazia!')
                else:
                    print('Lista de nomes em ordem alfabética:')
                    for nome in sorted(nomes):
                        print(nome)
            case 3:
                pesquisa = input('Digite o nome que está procurando: ').strip().capitalize()
                if pesquisa in nomes:
                    print(f'O nome {pesquisa} está na lista.')
                else:
                    print(f'Lamento, o nome {pesquisa} não foi encontrado na lista.')
            case 4:
                if not nomes:
                    print('A lista está vazia.')
                else:
                    for i in range(len(nomes)):
                        print(f'Índice {i}: {nomes[i]}')
                    alterar = int(input('Digite o índice do nome a ser alterado: '))
                    if 0 <= alterar < len(nomes):
                        print(f'Nome atual: {nomes[alterar]}')
                        nomes[alterar] = input('Digite o novo nome: ').strip().capitalize()
                        print('Nome alterado com sucesso.')
                    else:
                        print('Índice inválido.')
            case 5:
                if not nomes:
                    print('A lista está vazia.')
                else:
                    for i in range(len(nomes)):
                        print(f'Índice {i}: {nomes[i]}')
                    excluir = int(input('Digite o índice do nome que deseja excluir: '))
                    if 0 <= excluir < len(nomes):
                        confirma = input(f'Deseja excluir {nomes[excluir]}? (s/n): ').lower().strip()
                        if confirma == 's':
                            nome_removido = nomes.pop(excluir)
                            print(f'{nome_removido} removido com sucesso.')
                        else:
                            print('Exclusão cancelada.')
                    else:
                        print('Índice inválido.')
            case 6:
                print('Programa encerrado. Até mais!')
                break
            case _:
                print('Opção inválida. Escolha entre 1 e 6.')
    except ValueError:
        print('Entrada inválida. Digite um número entre 1 e 6.')

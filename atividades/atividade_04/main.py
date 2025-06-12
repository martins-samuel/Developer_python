'''Crie um programa em que o usuário pode escolher entre:
- Inserir um nome em uma lista 
- Exibir a lista de nomes 
- Pesquisar por um nome na lista 
- Sair do programa '''
import os 
nomes = []
while True:
    try:
        print('-'*45)
        print('Deseja inserir um nome em uma lista = 1 ')
        print('Deseja exibir a lista de nomes = 2 ')
        print('Deseja pesquisar por um nome na lista = 3')
        print('Sair do programa = 4')
        print('-'*45)
        entrada = int(input('Digite a opção escolhida: '))
        match entrada:
            case 1:
                nome_novo = input('Digite o nome que gostaria de adicionar: ').strip().upper()
                nomes.append(nome_novo)
            case 2:
                if not nomes:
                    print('A lista está vazia.')
                else:
                    print('Lista de nomes (ordenada):')
                    for nome in sorted(nomes):
                        print(f'- {nome}')
            case 3:
                pesquisa = input('Digite o nome que gostaria de buscar: ').strip().upper()
                if pesquisa in nomes:
                    print(f'O nome "{pesquisa}" está na lista.')
                else:
                    print(f'O nome "{pesquisa}" não foi encontrado na lista.')
            case 4:
                print('Programa encerrado')
                break
    except ValueError as e:
        print(f'Digite uma entrada válida')

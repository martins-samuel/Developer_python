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
        print('-'*55)
        print('Se deseja Inserir um nome na lista tecle = 1')
        print('Se deseja exibir a lista de nomes tecle = 2')
        print('Se deseja pesquisar um nome na lista tecle = 3')
        print('Se deseja alterar algum nome na lista tecle = 4')
        print('Se deseja excluir algum nome da lista tecle = 5')
        print('Se deseja sair do programa tecle = 6')
        print('-'*55)
        entrada = input('Digite a opção escolhida: ')
        int(entrada)
        os.system('cls')
        match entrada:
            case 1:
                nome_novo = input('Digite um novo nome na lista: ').strip().capitalize()
                nomes.append(nome_novo)
            case 2:
                if not nomes:
                    print('A lista está vazia! ')
                else:
                    print('A lista em ordem alfabética')
                    for nome in sorted(nomes):
                        print(nome)
            case 3:
                pesquisa = input('Digite o nome de quem você está procurando: ').strip().capitalize()
                if pesquisa in nomes:
                    print(f'O nome do {pesquisa} está na lista')
                else:
                    print(f'Lamento o nome do {pesquisa} não foi encotrando na lista')
            case 4:
                print(f'Lista dos nomes:\n')
                for i in range (len(nomes)):
                    print(f'Índice {i}: {nomes[i]}.')
                    alterar = input('Digite o indice do nome que gostaria de modificar: ')
                    int(alterar)
                    
    except ValueError as e:
        print('Digite uma opção válida entre 1 - 6')
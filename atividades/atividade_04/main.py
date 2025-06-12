'''Crie um programa em que o usuário pode escolher entre:
- Inserir um nome em uma lista 
- Exibir a lista de nomes 
- Pesquisar por um nome na lista 
- Sair do programa '''
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
                quantos_nomes_ja_tem = len(nomes)
                if quantos_nomes_ja_tem == 0:
                    print('Lista vazia')
                else:
                    for nome in nomes:
                        print(nome)
            case 3:
                pesquisa = input('Digite o nome que gostaria de buscar: ').strip().upper()
                print(f'O nome pesquisado está em {pesquisa}')
            case 4:
                print('Programa encerrado')
                break
    except ValueError as e:
        print(f'Digite uma entrada válida')
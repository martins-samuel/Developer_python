'''
Crie um programa que faça as seguintes operações:
-Inserir dados de novo usuário
-Exibir lista de usuários
-Alterar dados de um usuário já cadastrado
-Excluir usuários da lista 
-Sair do programa 
Os dados a serm cadastrados serão os seguintes:
-Nome;-Data de Nascimento;-Email;-CPF;-Telefone;-Profissão;-Gênero'''
import os
chaves = ('Nome ', 'Idade ', 'Email ', 'CPF ','Telefone ','Profissão ','Gênero ')
pessoas = []
while True:
    try:
        print('Deseja inserir um novo usuário = 1')
        print('Deseja exibir a lista de usuários = 2')
        print('Deseja alterar dados de um usuário já cadastrado = 3')
        print('Deseja excluir usuários da lista = 4  ')
        print('Deseja encerrar o programa = 5 ')
        escolha_usuario = int(input('Digite a sua escolha de usuário: '))
        os.system('cls')
        pessoa = {}
        match escolha_usuario:
            case 1:
                
                try:
                    for chave in chaves:
                        if chave == "Idade":
                            pessoa[chave] = int(input('Digite a idade'))
                        else:
                            pessoa[chave] = input(f'Informe {chave}')
                            print(f'{pessoa.get(chaves[0])} inserida com sucesso')
                    pessoas.append(pessoa)
                        
                except Exception as e:
                    print(f'Não foi possível cadastrar uma nova pessoa. {e}')
            case 2:
                    if not pessoas:
                        print('Não existe nenhuma pessoa cadastrada')
                    else:
                        print("\n--- Lista de Usuários ---")
                        for i, pessoa in enumerate(pessoas):
                            print(f"\nUsuário {i + 1}:")
                            for chave, valor in pessoa.items(): 
                                print(f'{chave}: {valor}') 
                            print('-' * 40) 
            case 3:
                000
            case 5:
                print('Programa encerrado com SUCESSO!')
                break

    except Exception as e:
        print(f'Entranda inválida tente novamente. {e}')
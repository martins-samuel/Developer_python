'''
Crie um programa  com um dicionário chamado "Usuário", com o seguinte menu:
-Cadastrar nova chave
-Exibir dadis do usuário
-Alterar valor da chave
-Excluir chave 
- Sair do programa
#NOTE - Os dados a serem inseridos precisam ter a ver com dados de usuário
'''
import os
usuario = {
    'nome' : "samuel",
    'idade' : 10,
    'email' : "samuel@gmail.com"
}
while True:

    print('Deseja cadastrar uma nova chave de usuário = 1 ')
    print('Deseja exibir os dados do usuário = 2')
    print('Deseja alterar o valor da chave = 3')
    print('Deseja excluir a chave do usuário = 4')
    print('Deseja sair do programa = 5')
    try:
        escolha = int(input('Digite a sua escolha: '))
        os.system('cls')
        match escolha:
            case 1:
                chave_nova = input('Digite o nome da nova chave que você deseja inserir: ').lower().strip()
                valor_novo = input(f'Digite o valor que a {chave_nova} vai receber : ')
                usuario[chave_nova] = valor_novo

            case 2:
                print('\n--- Dados do Usuário ---')
                for dados in usuario:
                    print(f'{dados.capitalize()} : {usuario.get(dados)}')
            case 3:
                chave_alterar = input('Informe o nome da chave que deseja alterar ').lower().strip()
                # tratamento de exceção
                try:
                    if chave_alterar in usuario:
                        usuario[chave_alterar]= input('Informe o novo valor: ').strip().lower()
                    else:
                        print('Não foi possível encontrar a chave requisitada. ')
                except Exception as e:
                    print(f'Não foi possível alterar {e}')
            case 4:
                chave_excluir = input('Informe o nome da chave que deseja deletar: ').lower().strip()
                # tratamento de exceção 
                try:
                    if chave_excluir in usuario:
                        del usuario[chave_excluir]
                        print('Chave excluída com sucesso!')
                except Exception as e:
                    print(f'Não foi possível deletar a chave. {e}.')
                finally:
                    #exibe os valores do dicinario
                    for chave_excluir in usuario:
                        print(f'{chave_excluir.capitalize()}: {usuario.get(chave_excluir)}')
            case 5:
                print('Program encerrado!')
                break
                
    except Exception as e:
        print(f'Entrada inválida {e}')


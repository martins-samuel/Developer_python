usuario = {
    'nome': 'Samuel',
    'idade': 10,
    'email': 'samuel@gmail.com'
}

while True:
    print('\n--- Menu do Usuário ---')
    print('1 - Cadastrar nova chave')
    print('2 - Exibir dados do usuário')
    print('3 - Alterar valor da chave')
    print('4 - Excluir chave')
    print('5 - Sair do programa')

    try:
        escolha = int(input('Digite a sua escolha: '))

        match escolha:
            case 1:
                print('\n--- Cadastrar Nova Chave ---')
                chave_nova = input('Digite o nome da nova chave (ex: "telefone", "endereco"): ').lower().strip()
                if chave_nova in usuario:
                    print(f"A chave '{chave_nova}' já existe. Deseja alterá-la? (s/n)")
                    confirmacao = input().lower().strip()
                    if confirmacao != 's':
                        continue
                valor_novo = input(f'Digite o valor para a chave "{chave_nova}": ').strip()
                usuario[chave_nova] = valor_novo
                print(f"Chave '{chave_nova}' cadastrada/atualizada com sucesso!")

            case 2:
                print('\n--- Dados do Usuário ---')
                if usuario:
                    for chave, valor in usuario.items():
                        print(f'{chave.capitalize()}: {valor}')
                else:
                    print('Nenhum dado de usuário cadastrado ainda.')

            case 3:
                print('\n--- Alterar Valor da Chave ---')
                if not usuario:
                    print('Nenhum dado de usuário para alterar.')
                    continue
                chave_alterar = input('Informe o nome da chave que deseja alterar: ').lower().strip()
                if chave_alterar in usuario:
                    novo_valor = input(f'Informe o novo valor para "{chave_alterar}": ').strip()
                    usuario[chave_alterar] = novo_valor
                    print(f"Valor da chave '{chave_alterar}' alterado com sucesso!")
                else:
                    print(f"A chave '{chave_alterar}' não foi encontrada.")

            case 4:
                print('\n--- Excluir Chave ---')
                if not usuario:
                    print('Nenhum dado de usuário para excluir.')
                    continue
                chave_excluir = input('Informe o nome da chave que deseja deletar: ').lower().strip()
                if chave_excluir in usuario:
                    del usuario[chave_excluir]
                    print(f"Chave '{chave_excluir}' excluída com sucesso!")
                    print('\nDados restantes:')
                    if usuario:
                        for chave, valor in usuario.items():
                            print(f'{chave.capitalize()}: {valor}')
                    else:
                        print('Todos os dados foram excluídos.')
                else:
                    print(f"A chave '{chave_excluir}' não foi encontrada.")

            case 5:
                print('Programa encerrado! Até mais.')
                break

            case _: # Caso padrão para qualquer outra entrada inválida
                print('Opção inválida. Por favor, digite um número entre 1 e 5.')

    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro correspondente à opção desejada.')
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')
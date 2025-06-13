# dicionário 
pessoa ={
    'nome' : 'Alex Machado',
    'email' : 'Alex@gmail.com'
}
#exibe os dados 
print(f'Nome: {pessoa['nome']}')
print(f'Email: {pessoa.get('email')}')

#exibe dados inexistentes
print(f'Idade: {pessoa.get('idade')}')
#inserindo a idade na pessoa
try:
    pessoa['idade'] = int(input('informe a idade: '))
except Exception as e:
    print(f'Não foi possível inserir o novo valor {e}')
finally:
    print(f'Nome: {pessoa.get('nome')}')
    print(f'Email: {pessoa.get('email')}')
    print(f'Idade: {pessoa.get('idade')}')

# lista de dicionários
pessoas = [
    {
        'nome' : "Fulano",
        'idade' : 18,
        'email' : "fulano@gmail.com",
        'profissão ' : "Programador"
    },
    {
        'nome' : "Cicrano",
        'idade' : 25,
        'email' : "cicrano@gmail.com",
        'profissão' : "DBA"
    },
    {
        'nome' : "Beltrano",
        'idade' : 30,
        'email' : "beltrano@gmail.com",
        'profissão' : "Gerente de Projetos"
    }
]
#exibição dis dados dos dicionários da lsta 
for pessoa in pessoas:
    print('-'*55)
    print('\n')
    for chave in pessoa:
        print(f'{chave.capitalize()}: {pessoa.get(chave)}')
nova_pessoa = {
    'nome' : "Alex Machado",
    'idade' : "alex@gmail.com",
    'profissão' : "CEO"
}
# adicionando novo dicionário à lista 
pessoas.append(nova_pessoa)
 # exibe nova lista de dicionários 
print('\nNova Lista \n')
for pessoa in pessoas:
    print('-'*55)
    print('\n')
    for chave in pessoa:
        print(f'{chave.capitalize()}: {pessoa.get(chave)}')


# lista de cidades 
cidades = [
    'Brasília',
    'Rio de Janeiro',
    'São Paulo',
    'Goiânia',
    'Palmas',
    'São luís',
    'Belém',
    'Fortaleza',
    'Salvador',
    'Porto Alegre',
    'Florianópolis',
    'Belo Horizonte',''
    'Brasília',
    'Maceió',
    'Goiânia'
]
#usuário faz a pesquisa
''' 


if pesquisa in cidades:
    print(f'{pesquisa} encontrada')
else:
    print(f'{pesquisa} não encontrada')
''' 
pesquisa = input('Informe o nome da cidade a ser pesquisada: ').title().strip()
quantidade = cidades.count(pesquisa)
print(f'{pesquisa} foi encontrado {quantidade} vezes na lista')
#tupla 
chaves = ('Nome ', 'Idade ', 'Email ', 'Profissão ')
pessoas = [
{
    chaves[0]: "Alex Machado",
    chaves[1]: 40,
    chaves[2]: "Alex@gmail.com",
    chaves[3]: "CEO"
},
{
    chaves[0]: "Maria da Silva",
    chaves[1]: 25,
    chaves[2]: "maria@gmail.com",
    chaves[3]: "Assistente administrativo"
}
    
]
# inserindo um novo dicionário 
pessoa = {}
# Inserindo dados no novo dicionário 
try:
    for chave in chaves:
        if chave == "Idade": 
            pessoa[chave] = int(input('Informe a Idade'))
        else:
            pessoa[chave] = input(f'Informe {chave}')
    pessoas.append(pessoa)
    print(f'{pessoa.get(chaves[0])} inserida com sucesso')
except Exception as e:
    print(f'Não foi possível cadastrar uma nova pessoa. {e}')
finally:
    for pessoa in pessoas:
        for chave in pessoa:
            print(f'{chave} : {pessoa.get(chave)}')
    
#tupla
estados = (
    'Distrito Federal','Goiás','Minas Gerais','Tocantins','Rio De Janeiro','Ceará'
)
#Lista a tupla 
for estado in estados:
    print(estado)

estado_pesquisa = input('Informe um estado que deseja pesquisar: ').title().strip()
qtde_estados = estados.count(estado_pesquisa)
print(f'{estado_pesquisa} foi encontrado {qtde_estados} vezes na tupla')
# tentando acrescentar item na tupla 
try:
    novo_estado = input('Informe o nome do estado que deseja imserir').title().strip()
    estados.append(novo_estado)
    for estado in estados:
        print(estado)
except Exception as e:
    print(f'Não é possível adiconar a tupla. {e} ')
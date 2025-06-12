# declaração de lista 
carrinho = []

while True:
    item = input('Informe o item : ').capitalize().strip()
    carrinho.append(item)
    print(f'{item} inserido no carrinho com sucesso!')
    confirmar = input('Deseja inserir outro item (s/n)').lower().strip()
    match confirmar:
        case 's':
            continue
        case 'n':
            break
        case _:
            print('Opção inválida')
            continue
# ordena a lista na ordem alfabetica 
carrinho.sort()
# exive os itens da lista 
for item in carrinho: 
    print(item)
# dicionario 
usuario = {
    'nome' : "Alex Machado",
    'idade' : 30,
    'email' : "alex@gmail.com",
    'profissao' : "Programador"
}
chave = input('Informe o nome da chave que deseja deletar: ').lower().strip()
# tratamento de exceção 
try:
    if chave in usuario:
         del usuario[chave]
         print('Chave excluída com sucesso!')
except Exception as e:
    print(f'Não foi possível deletar a chave. {e}.')
finally:
     #exibe os valores do dicinario
     for chave in usuario:
          print(f'{chave.capitalize()}: {usuario.get(chave)}')
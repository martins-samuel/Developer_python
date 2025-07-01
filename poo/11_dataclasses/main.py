from classes import Pessoa 

if __name__ == "__main__":
    usuario = Pessoa(
        nome="",
        idade = 0,
        email="",
        telefone="",
        profissao="",
        peso=0.0,
        altura=0.0
    )
    usuario.nome = "Fulano"
    usuario.idade = 18
    usuario.email = "fulano@gmail.com"
    usuario.profissao = "Programador"
    usuario.peso = 100
    usuario.altura = 1.85
print(f"{usuario}, tenho {len(usuario)}. Segue os meus dados")
print(f"O meu nome é {usuario.nome} tenho {usuario.idade} meu email é {usuario.email} meu telefone {usuario.telefone} minha profissão é {usuario.profissao} peso {usuario.peso} KG e tenho {usuario.altura} de altura em Metros")
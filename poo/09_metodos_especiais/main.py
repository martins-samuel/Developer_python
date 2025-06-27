from classes import Pessoa
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")
if __name__ == "__main__":
    try:
        usuario = Pessoa(nome="",profissao="",idade="")
        usuario.nome = input("Informe o nome: ").strip().title()
        usuario.profissao = input("Informe a profissão: ").strip()
        usuario.idade = int(input("Digite a sua idade: "))
    except Exception as e:
        print(f"Não foi possível executar o programa. {e}")
    limpar()
    print(usuario)
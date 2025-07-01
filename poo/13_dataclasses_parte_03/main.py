from classes import PessoaFisica, PessoaJuridica
import os 
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = PessoaFisica(nome="",profissao="",genero="",email="",telefone="",endereco="")
    empresa = PessoaJuridica(nome_fantasia="",cnpj="",website="",email="",telefone="",endereco="")

    limpar()

    print(f"{'-'*25} Dados do Usuário {'-'*25}")
    usuario.nome= input("Informe o nome do usuário: ").strip().title()
    usuario.genero= input("Informe o genero do usuário: ").strip()
    usuario.profissao= input("Informe a profissão do usuário: ").strip()
    usuario.email= input("Informe o email do usuário: ").strip().lower()
    usuario.telefone= input("Informe o telefone do usuário: ").strip()
    usuario.endereco= input("Informe o endereço do usuário: ").strip().title()

    print(f"{'-'*25}Informe os dados da Empresa:{'-'*25}\n")
    empresa.nome_fantasia = input("Informe o nome fantasia da empresa: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.website= input("Informe o website : ").strip().lower()
    empresa.email = input("Informe o email da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ").strip().title()

    print(f"{usuario}.Segue os dados")
    usuario.exibir_dados()
    print(f"{empresa}. Segue os dados da empresa")
    empresa.exibir_dados()

    del(usuario)
    del(empresa)
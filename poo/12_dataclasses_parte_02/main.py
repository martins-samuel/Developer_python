from classes import PessoaFisica,PessoaJuridica
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = PessoaFisica(
    nome="",
    cpf="",
    profissao="",
    email="",
    telefone="",
    endereco="",
    )
    empresa = PessoaJuridica(
        razao_social="",
        nome_fantasia="",
        cnpj="",
        email="",
        telefone="",
        endereco=""
    )
    print("Informe os dados do USUÁRIO:\n")
    usuario.nome= input("Informe o nome do usuário: ").strip().title()
    usuario.cpf= input("Informe o CPF do usuário: ").strip()
    usuario.profissao= input("Informe a profissão do usuário: ").strip()
    usuario.email= input("Informe o email do usuário: ").strip().lower()
    usuario.telefone= input("Informe o telefone do usuário: ").strip()
    usuario.endereco= input("Informe o endereço do usuário: ").strip().title()
    print('-'*45)

    print("Informe os dados da Empresa:\n")
    empresa.razao_social= input("Informe a razão social: ").strip().title()
    empresa.nome_fantasia = input("Informe o nome fantasia da empresa: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.email = input("Informe o email da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ").strip().title()
    print('-'*45)
    limpar()
    #saída de dados
    print(usuario)
    print(empresa)
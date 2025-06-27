from classes import PessoaFisica, PessoaJuridica
import os 
def limpar():
    os.system("cls" if os.name == "nt" else "clear")
if __name__ == "__main__":
    usuario = PessoaFisica(nome= "",cpf= "", profissao= "", email= "", telefone= "")
    empresa = PessoaJuridica(razao_social= "", nome_fantasia= "", cnpj= "", email= "", telefone= "")

    print(f"{'-'*20} Dados do Usuário {'-'*20}")
    usuario.nome = input("Informe o nome: ").title().strip()
    usuario.cpf = input("Informe o cpf: ").strip()
    usuario.profissao = input("Informe a profissão: ").strip()
    usuario.telefone = input("Informe o telefone: ").strip()
    usuario.email = input("Informe o email: ").strip().lower()
    limpar()

    print(f"{'-'*20} Dados da empresa {'-'*20}")
    empresa.razao_social =input("Informe  a razão social: ").title().strip()
    empresa.nome_fantasia =input("Informe  o nome fantasia : ").title().strip()
    empresa.cnpj =input("Informe  o CNPJ: ").strip()
    empresa.email =input("Informe  o E-mail : ").lower().strip()
    empresa.telefone =input("Informe  o telefone: ").strip()
    limpar()

    print(f"{'-'*20} Dados do Usuário {'-'*20}")
    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"Profissão: {usuario.profissao}")
    print(f"E-mail: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")

    print(f"{'-'*20} Dados da empresa {'-'*20}")
    print(f"Razão social: {empresa.razao_social}")
    print(f"Nome da empresa: {empresa.nome_fantasia}")
    print(f"CNPJ: {empresa.cnpj}")
    print(f"E-mail da empresa: {empresa.email}")
    print(f"Telefone da empresa: {empresa.telefone}")









#bibliotecas 
import os
import classes

if __name__ == "__main__": 
#instância de objetos
    usuario = classes.PessoaFisica("","","","","","","")
    empresa= classes.PessoaJuridica("","","","","","")

    #limpar a tela
    os.system("cls" if os.name == "nt" else "clear")

#atribui valores ao objeto do tipo Pessoa física
    print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}\n")
    usuario.nome = input("Informe seu nome: ").title().strip()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.profissao = input("Informe seu gênero ").strip()
    usuario.genero = input("Informe sua profissão ").strip()
    usuario.email = input("Informe seu e-mail ").strip().lower()
    usuario.endereco = input("Informe seu endereço: ").strip().title()
    usuario.telefone = input("Informe seu telefone: ").strip()
#limpar a tela
os.system("cls" if os.name == "nt" else "clear")

#atribui valores  ao objeto do tipo pessoa juridica
empresa.razao_social = input("Informe a razão social da empresa: ").title().strip()
empresa.nome_fantasia = input ("Informe o nome fantansia ").title().strip()
empresa.cnpj = input("Informe o cnpj: ").strip()
empresa.email = input("Informe o e-mail: ").strip().lower()
empresa.endereco = input("Informe o endereço da empresa").strip().title()
empresa.telefone = input("Informe o telefone da empresa: ").strip()
# limpa a tela
os.system("cls" if os.name == "nt" else "clear")
#exibir os dados do usuário e da empresa
print("Dados do usuário:\n")
usuario.exibir_dados()
print("Dados da empresa:\n")
empresa.exibir_dados()
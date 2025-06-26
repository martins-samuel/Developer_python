#importações
import classes
import os 
if __name__ == "__main__":
    #instância objeto
    usuario = classes.PessoaFisica("", "", "", "","","")
    empresa = classes.PessoaJuridica("", "", "", "","","")
while True:
    print("1- Inserir dados do usuário")
    print("2- Inserir dados da empresa")
    print("3- Sair do programa")  
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            try:
                usuario.nome = input("Informe o nome do usuário: ").title().strip()
                usuario.cpf = input("Informe o CPF do usuário: ").strip()
                usuario.profissao = input("Informe a profissão do usuário: ").strip()
                usuario.email = input("Informe o E-mail do usuário: ").strip().lower()
                usuario.endereco = input("Informe o endereço: ").strip().title()
                usuario.telefone = input("Informe o telefone: ").strip()
                os.system("cls" if os.name == "nt" else "clear")
                print(f"dados de {usuario.nome} inseridos com sucesso! ")   
            except Exception as e:
                print(f" Não foi possível inserir dados do usuário. {e}")
        case "2":
            try:
                empresa.razao_social = input("Informe a razão social da empresa: ").strip().title()
                empresa.nome_fantasia = input("Informe o nome fantasia da empresa: ").strip().title()
                empresa.cnpj = input("Informe o cnpj da empresa: ").strip()
                empresa.email = input("Informe o e-mail da empresa").strip()
                empresa.endereco = input("Informe o endereço da empresa: ").strip()
            except Exception as e:
                ...
        case "3":
            print("Programa encerrado")
            break
        case _:
            print("Opção inválida")
            continue        
    
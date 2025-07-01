from dataclasses import dataclass

@dataclass
class Pessoa:
    email: str
    telefone: str 
    endereco: str 

@dataclass
class PessoaFisica(Pessoa):
    nome: str
    cpf: str
    profissao: str 


    def __str__(self):
        return (f"Olá, meu nome é {self.nome},\n"
                f"trabalho como {self.profissao},\n"
                f"meu CPF é {self.cpf},\n"
                f"meu e-mail é {self.email},\n"
                f"meu telefone é {self.telefone},\n"
                f"e meu endereço é {self.endereco}.")

    def __del__(self):
        print(f"Objeto {self.nome} destruído com sucessor")

@dataclass
class PessoaJuridica(Pessoa):
    razao_social: str
    nome_fantasia: str 
    cnpj: str 

    def __str__(self):
        return (f"Olá, Somos da empresa {self.nome_fantasia},\n"
                f"da razão social {self.razao_social},\n"
                f"e meu CNPJ é {self.cnpj},\n"
                f"meu e-mail é {self.email},\n"
                f"meu telefone é {self.telefone},\n"
                f"e o meu endereço é {self.endereco}.")

    def __del__(self):
        print(f"Objeto {self.nome_fantasia} destruído com sucesso")
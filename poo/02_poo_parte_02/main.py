# classe 
class Pessoa:
    nome = "Samuel Martins"
    idade = 40
    email = "samuel@gmail.com"
    profissao = "programador"

    # métodos
    def apresentar(self):
        print(f'Olá meu nome é {self.nome}, tenho  {self.idade}, de idade trabalho como {self.profissao} e meu e-mail é {self.email}')

# algoritmo principal 
if __name__ == "__main__":
    # instância a classe
    usuario = Pessoa()
    # executar o método 
    usuario.apresentar()
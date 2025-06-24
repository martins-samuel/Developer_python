import random  # necessário para usar random.getrandbits()

class Pessoa:
    #construtor
    def __init__(self,nome,email,profissao):
        self.nome = nome
        self.email = email
        self.profissao = profissao

    # métodos 
    def dar_boas_vindas(self):
        return"Olá, boa tarde!"
    
    def cumprimentar(self):
        return f"Olá, eu me chamo {self.nome}. É um prazer !"
    
    def perguntar(self):
        return f"Qual o seu nome? "
    
    def cartao_de_visitas(self):
        print(f"nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Profissão: {self.profissao}")
    
    def ofender (self,nome):
        return f"Quem liga {nome}? Me erra! Vai ver se eu estou na esquina!"


#algoritmo principal
if __name__ == "__main__":
    #instancia de dois objetos 
    usuario_masculino = Pessoa("","","")
    usuario_feminino = Pessoa("","","")

    # define atributo humor
    usuario_masculino.humor = bool(random.getrandbits(1))
    usuario_feminino.humor = bool(random.getrandbits(1))
    
    #seta os valores dos atributos do objeto masculino 
    usuario_masculino.nome = input("Informe seu nome: ").title().strip()
    usuario_masculino.email = input('Informe seu e-mail: ').strip().lower()
    usuario_masculino.profissao = input('Informe sua profissão: ').strip()

    #seta os valores dos atributos do objeto feminino 
    usuario_feminino.nome = input("Informe seu nome: ").title().strip()
    usuario_feminino.email = input('Informe seu e-mail: ').strip().lower()
    usuario_feminino.profissao = input('Informe sua profissão: ').strip()

    #conversa
    print(f"Homem: -{usuario_masculino.dar_boas_vindas()}")
    print(f"Mulher: -{usuario_feminino.dar_boas_vindas()} ")
    print(f"Homem: -{usuario_masculino.perguntar()}")
    if usuario_feminino.humor is True:
        print(f"Mulher: -{usuario_feminino.cumprimentar()}")
        print(f"Mulher: -{usuario_feminino.perguntar()}")
        usuario_masculino.humor = usuario_feminino.humor
        print(f"Homem: -{usuario_masculino.cumprimentar()}")
        print(f"Homem: Bom humor = {usuario_masculino.humor}")
        print(f"Segue o meu cartão de visistas")
        usuario_masculino.cartao_de_visitas()
    else:
        print(f"Mulher: -{usuario_feminino.ofender(usuario_masculino.nome)}")
        usuario_masculino.humor = usuario_feminino.humor
        print(f"Homem: Bom humor = {usuario_masculino.humor}")

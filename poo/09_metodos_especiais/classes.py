class Pessoa:
    def __init__(self,nome,profissao,idade):
        self.nome = nome 
        self.profissao = profissao 
        self.idade = idade 

    def __str__(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} de idade  e trabalho com {self.profissao}"
"""#TODO - atividade: Crie um programa que receba 
os dados de dois objetos diferentes da mesma classe Pessoa.
Os dados serão os seguintes: 
-Nome
-idade 
-email 
-telefone
-gênero
-tipo sanguíneo 
- Já teve doença transmitida por sangue ? 
Suponha que o objeto 'usuario_2' esteja precisando de doação de sangue do 'usuario_1'
O programa deve informar os dados dos dois usuários, e ao final, 
informar se o usuario_1 pode doar sangue para o usuario_2 ou não
NoTe - as duas última perguntas deverá ter uma resposta randômica  """
class Pessoa:
    #construtor 
    def __init__(self, nome, idade, email, telefone, genero, tipoSanguineo,doenca):
        self.nome = nome 
        self.idade = idade 
        self.email = email
        self.telefone = telefone 
        self.genero = genero
        self.tipoSanguineo = tipoSanguineo
        self.doenca = doenca 
    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'E-mail: {self.email}')
        print(f'Telefone: {self.telefone}')
        print(f'Gênero: {self.genero}')
        print(f'Tipo sanguíneo: {self.tipoSanguineo}')
        print(f'Já teve doença transmitida pelo sangue ? {self.doenca}')






        # entrada de dados para usuários 
        print('\/\/\/\/ Dados do usuário_1 \/\/\/')
        
        nome1 = input('Qual é o seu nome ? ').title().strip()
        idade1 = int(input('Qual a sua idade ?'))
        email1 = input('Digite o seu email: ').strip()
        telefone = input('Digite o seu número de telefone: ').strip()
        genero = input('Digite o seu gênero H = homem ou M = mulher ou O = outros ').upper().strip()
        tipo_sanguineo = input('Digite o seu tipo sanguíneo: ').strip().upper()
        

#TODO - atividade: Crie um programa que receba do usuário os seguintes dados:
'''
- Nome
- Cpf
- Data de Nascimento 
- Email 
- Gênero
- Telefone
- Enderenço
- Altura em metros 
- Peso em kg 
- Tipo Sanguíneo
Ao final exiba para o usuário os dados
'''
import os
pessoa = {
    'Nome' : '',
    'Cpf' :'' ,
    'Data_nascimento' : '',
    'Email' :'' ,
    'Gênero ':'' ,
    'Telefone ':'' ,
    'Enderenco ':'' ,
    'Altura_metros ':'',
    'Peso_KG':'',
    'Tipo_sanguíneo':'',
}
try:
    pessoa['Nome'] = input('Informe o nome: ').strip().capitalize()
    pessoa['Cpf'] = input('Informe o seu cpf: ').strip()
    pessoa['Data_nascimento'] = input('Digite a data de nascimento: (DD/MM/AAAA) ').strip()
    pessoa['Email'] = input('Digite o email').strip()    
    pessoa['Gênero'] = input('Informe o gênero (Ex: M/F/Outro): ').strip().capitalize()
    pessoa['Telefone'] = input('Informe o  número de telefone (Ex: DDD XXXXX-XXXX):').strip()
    pessoa['enderenco'] = input('informe o endereço: ').strip()
    pessoa['Altura_metros'] = float(input('Informe a altura em metros: ').replace(',','.'))
    pessoa['Peso_kg'] = float(input('Informe o peso em kg: ').replace(',','.'))
    pessoa['Tipo_Sanguineo'] = input('Informe o tipo sanguíneo: ').strip().upper()
    os.system('cls')
except Exception as e:
    print(f'Não foi possível inserir o novo valor {e}')
finally:

    print('\n--- Dados do Usuário ---')
    print(f"Nome: {pessoa.get('Nome')}") 
    print(f"CPF: {pessoa.get('Cpf')}") 
    print(f"Data de Nascimento: {pessoa.get('Data_nascimento')}") 
    print(f"Email: {pessoa.get('Email')}") 
    print(f"Gênero: {pessoa.get('Genero')}") 
    print(f"Telefone: {pessoa.get('Telefone')}") 
    print(f"Endereço: {pessoa.get('Endereco')}") 
    print(f"Altura: {pessoa.get('Altura_metros', 0.0):.2f} m") 
    print(f"Peso: {pessoa.get('Peso_kg', 0.0):.2f} kg") 
    print(f"Tipo Sanguíneo: {pessoa.get('Tipo_Sanguineo')}") 
    print('-'*50)


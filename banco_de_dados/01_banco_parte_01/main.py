from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os 

def limpar():
    os.system("cls" if os.name == "nt" else "clear")
try:
    engine = create_engine("sqlite:///meu_primeiro_banco.db")
    Base = declarative_base()

    # Cria a entidade Pessoa
    class Pessoa(Base):
        __tablename__ = "pessoa"
        
        id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String, nullable=False)
        data_nasc = Column(Date, nullable=False)
        email = Column(String, nullable=False, unique=True)
        cpf = Column(String, nullable=False, unique=True)
        genero = Column(String, nullable=True)
        tipo_sanguineo = Column(String, nullable=True)

    Base.metadata.create_all(engine)
    #print("Entidade Pessoa criada com sucesso")"No futuro deletar"
except Exception as e:
    print(f"Erro no sistema. {e}")

try: 
    Session = sessionmaker(bind=engine)
    session = Session()

    # Entrada de dados do usuário
    nome = input("Informe o nome: ").strip().title()
    data_nasc_str = input("Informe a data de nascimento: (dd/mm/aaaa) ").strip()
    data_nasc = datetime.strptime(data_nasc_str, "%d/%m/%Y").date()
    email = input("Informe o email: ").strip().lower()
    cpf = input("Informe o cpf: ").strip()
    genero = input("Informe o gênero: ").strip()
    tipo_sanguineo = input("Informe o tipo sanguíneo: ").strip().upper()

    # Cria nova pessoa
    nova_pessoa = Pessoa(
        nome=nome,
        data_nasc=data_nasc,
        email=email,
        cpf=cpf,
        genero=genero,
        tipo_sanguineo=tipo_sanguineo
    )

    # Adiciona e confirma no banco
    session.add(nova_pessoa)
    session.commit()
    print("Pessoa cadastrada com sucesso")

    #deletar no futuro session.close()
except Exception as e:
    print(f"Não foi possível cadastrar novo usuário: {e}")

pessoas = session.query(Pessoa).all()
print(f"\n{'-'*20} Pessoas Cadastradas {'-' * 20}")
for pessoa in pessoas:
    print(f"Id: {pessoa.id_pessoa}")
    print(f"Nome: {pessoa.nome}")
    print(f"Data de nascimento: {pessoa.data_nasc.strftime('%d/%m/%Y')}")
    print(f"E-mail: {pessoa.email}")
    print(f"Gênero: {pessoa.genero}")
    print(f"Tipo sanguíneo: {pessoa.tipo_sanguineo}")
    print(f"{'-' * 60}")
session.close()

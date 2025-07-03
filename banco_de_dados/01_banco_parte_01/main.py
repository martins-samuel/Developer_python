from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

try:
    engine = create_engine("sqlite:///meu_primeiro_banco.db")
    Base = declarative_base()

    # Cria a entidade Pessoa
    class Pessoa(Base):
        __tablename__ = "pessoa"
        
        # Atributos 
        id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String, nullable=False)
        # FIXME data_nascimento = Column(Date, nullable=False)
        email = Column(String, nullable=False, unique=True)
        cpf = Column(String, nullable=False, unique=True)
        genero = Column(String, nullable=True)
        tipo_sanguineo = Column(String, nullable=True)
        #cria a tabela
    Base.metadata.create_all(engine)
    print("Entidade Pessoa criada com sucesso")
except Exception as e:
    print(f"Erro no sistema. {e}")
try: 
    Session = sessionmaker(bind=engine)
    session = Session()

    #cadastrar usuário no banco 
    nome = input("Informe o nome: ").strip().title()
    #data_nasc = input("Informe a data de nascimento: (aaaa-mm-dd) ").strip().lower()
    email = input("Informe o email ").strip().lower()
    cpf = input("Informe o cpf ").strip()
    genero = input("Informe o gênero: ").strip()
    tipo_sanguineo = input("Informe o tipo sanguineo : ").strip().upper()

    nova_pessoa = Pessoa(
        nome = nome,
        #data_nasc = data_nasc, 
        email = email, 
        cpf = cpf,
        genero = genero,
        tipo_sanguineo = tipo_sanguineo
    )

    session.add(nova_pessoa)
    session.commit()
    print("Pessoa cadastrada com sucesso")

    session.close()
except Exception as e:
    print(f"Não foi possível cadastrar novo usuário {e}")
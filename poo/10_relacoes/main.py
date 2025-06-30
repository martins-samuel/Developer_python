'''from classes import Aluno, Curso

if __name__ == "__main__":
    aluno01 = Aluno("Fulano",101,"111.111.111.-11")
    aluno02 = Aluno("Cicrano",102,"222.222.222-22")
    aluno03 = Aluno("Beltrano",103,"333.333.333-33")
    aluno04 = Aluno("João",104,"444.444.444-44")
    aluno05 = Aluno("Maria",105,"555.555.555-55")
    aluno06 = Aluno("Josè",106,"666.666.666-66")

    #cursos
    curso01 = Curso("Python Developer")
    curso02 = Curso("Ia com Python")
    curso03 = Curso("Desenvolvedor Java")

    #inscrevendo os alunos 
    aluno01.inscrever_curso(curso01)
    aluno02.inscrever_curso(curso01)
    aluno03.inscrever_curso(curso01)

    aluno04.inscrever_curso(curso02)
    aluno05.inscrever_curso(curso02)

    aluno06.inscrever_curso(curso03)
    #mostrar alunos no curso
    print(f"Cursos {curso01.nome_curso} tem os alunos: {curso01.listar_alunos()}")'''
from classes import Aluno, Curso
import os 
def limpar():
    os.system("cls" if os.name == "nt" else "clear")
if __name__ == "__main__":
    alunos = []
    cursos = []
    matricula = 0
    limpar()
    while True:
        aluno = Aluno(nome="",matricula=0,cpf="")
        curso = Curso(nome_curso="")
        
        print(f"{'-' *20} SISTEMA ESCOLAR {'-' *20}")
        print("1- Cadastrar Aluno")
        print("2- Cadastrar Curso")
        print("3- Matricula aluno no Curso")
        print("4- Listar Curso")
        print("5- Listar Aluno ")
        print("6- Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()

        limpar()

        match opcao:
            case "1":
                try:
                    matricula += 1
                    aluno.nome = input("Informe o nome do aluno: ").strip().title()
                    aluno.cpf = input("Informe o CPF do aluno: ").strip
                    aluno.matricula = matricula 
                    alunos.append(aluno)
                    print(f"Aluno {aluno.nome} matriculado com sucesso")

                except Exception as e:
                    print(f"Não foi possível cadastrar aluno {e}")
            case "2":
                try:
                    curso.nome_curso = input("Informe o curso: ").strip().title()
                    cursos.append(curso)
                    limpar()
                except Exception as e:
                    print(f"Não foi possível cadastrar curso. {e}")
                finally:
                    continue

            case "3":
                try:
                    print(f"{'-'*10} LISTA de ALUNOS {'-'*10}")
                    for aluno in alunos:
                        print(f"Nome: {aluno.nome}")
                        print(f"Matricula: {aluno.matricula}")
                        print(f"Cpf: {aluno.cpf}")
                        print('-'*40)
                    inscricao =int(input('Informe a matricula: '))
                    if inscricao in alunos:
                        aluno.nome = alunos.nome 
                        aluno.matricula = alunos.matricula 
                        aluno.cpf = alunos.cpf 
                        print(f"{'-' * 10} Lista de cursos {'-' * 10}")
                        for curso in cursos:
                            print(f"Curso: {curso.nome_curso}")
                        curso_inscricao = input("Informe o curso desejado").strip().title()
                        aluno.inscrever_curso(curso_inscricao)
                        limpar()
                        print(f"Aluno {aluno.nome} inscrito no curso {curso.nome_curso} com sucesso")
                    # else:
                    #     print("Não foi possível encontrar a matricula")
                except Exception as e:

                    print(f"Não foi possível matricular aluno no curso {e}")
                finally:
                    continue
                
            case "4":
                cursos.nome_curso.sort()
                for curso in cursos:
                    print(f"Curso: {curso.nome_curso}")
                    print("Alunos")
                    alunos.listar_alunos().sort()
                    for aluno in curso.listar_alunos():
                        print(aluno)
                    print('-'*40)
            case "5":
                alunos.nome.sort()
                for aluno in alunos:
                    print(f"Nome: {aluno.nome}")
                    print(f"Matrícula: {aluno.matricula}")
                    print(f"CPF: {aluno.cpf}")
                    print("Curso matriculado: ")
                    for curso in aluno.listar_cursos():
                        print(curso)
                    print('-'*40)
            case "6":
                print("Programa encerrado")
                break
            case _:
                print("opção inválida")
                continue
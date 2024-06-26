from Database import db
from livro import Livro
from Usuario import Usuario
from DataDeDevolucao import estimar_data_devolucao


def main():
    print("+" + "=" * 98 + "+")
    print("| " + " " * 26 + "BEM-VINDO AO GERENCIADOR DE BIBLIOTECA" + " " * 33 + "|")
    print("+" + "=" * 98 + "+")

    while True:
        print("="*100)
        print("[1] Adicionar usuário")
        print("[2] Adicionar novo livro")
        print("[3] Realizar empréstimo")
        print("[4] Inserir devolução")
        print("[5] Mostrar livros")
        print("[6] Mostrar usuários")
        print("[7] Ver livros emprestados")
        print("[0] Sair")

        opcao = input("\nDigite a opção desejada: ")
        if opcao == "1":
            nome = input("Nome do usuário: ")
            sobrenome = input("Sobrenome: ")
            endereco = input("Endereço: ")
            email = input("Email: ")
            telefone = input("Telefone: (exemplo:19123456789)")
            novo_usuario = Usuario(nome, sobrenome, email, endereco, telefone)
            db.add_usuario(novo_usuario)

        elif opcao == "2":
            titulo = input("Titulo:")
            autor = input("Nome do autor(a):")
            editora = input("Editora:")
            categoria = input("Categoria do livro:")
            novo_livro = Livro(titulo, autor, editora, categoria)
            db.add_livro(novo_livro)

        elif opcao == "3":
            perguta = input("Checar ID do livro? [y] ou [n]")
            resposta = perguta.lower()
            if resposta == "y":
                titulo = input("Digite o título: ")
                db.filtrar_por_titulo(titulo)
            id_livro = input("Insira o ID do livro: \n")
            pergunta2 = input("Checar o ID do usuario?[y] ou [n]")
            resposta1 = pergunta2.lower()
            if resposta1 == "y":
                nome_usuario = input("Digite o nome do usuario: ")
                db.filtrar_por_usuario(nome_usuario)
            id_usuario = input("ID do usuário: ")
            print("Exemplo data: 17-06-2024")
            data_emprestimo = input("Data do emprestimo: ")
            data_devulucao = estimar_data_devolucao(data_emprestimo)
            print(f"O livro deve ser devolvido até 30 dias -> {data_devulucao}")
            db.emprestar_livro(id_livro, id_usuario, data_emprestimo, None)

        elif opcao == "4":
            perguta = input("Checar ID do livro? [y] ou [n]")
            resposta = perguta.lower()
            if resposta == "y":
                titulo = input("Digite o título: ")
                db.filtrar_por_titulo(titulo)
            id_livro = int(input("Digite o ID do livro que está sendo devolvido: "))
            data_devolucao = input("Digite a data da devolução: ")
            db.inserir_data_devolucao(id_livro, data_devolucao)

        elif opcao == "5":
            opcao1 = input("Você deseja filtrar de alguma forma sua pesquisa?\n"
                           "[1] - Título \n" "[2] - Autor \n" "[3] - Categoria \n" "[0] - Não quero filtrar\n")

            if opcao1 == "1":
                titulo = input("Digite o título: ")
                db.filtrar_por_titulo(titulo)
            elif opcao1 == "2":
                autor = input("Digite o/a autor/a desejado: ")
                db.filtrar_por_autor(autor)
            elif opcao1 == "3":
                categoria = input("Digite a categoria desejada: ")
                db.filtrar_por_categorias(categoria)
            elif opcao1 == "0":
                db.listar_livros()

        elif opcao == "6":
            escolha = input("[1] - Usuário especifico \n[2] - listar todos\n")
            if escolha == "1":
                nome_usuario = input("Digite o nome do usuario: ")
                db.filtrar_por_usuario(nome_usuario)
            else:
                db.listar_usuarios()

        elif opcao == "7":
            db.exibir_emprestados()

        elif opcao == "0":
            print("Saindo...")
            return False

        else:
            print("=" * 100)
            print("Opção invalida, tente novamente!")

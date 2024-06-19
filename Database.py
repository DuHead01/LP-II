import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host='localhost', user="root", password="1234", database="biblioteca"):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                self.create_table()
        except Error as e:
            print(f"Erro enquanto conecta no MySQL: {e}")

    #Cria tebela caso ela não exista
    def create_table(self):
        try:
            self.cursor.execute("""create table if not exists livros(
                                    id int auto_increment primary key,
                                    titulo varchar(255)not null,
                                    autor varchar(255)not null,
                                    editora varchar(255)not null,
                                    categoria varchar(255)not null);""")

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS USUARIOS(
               id int auto_increment primary key,
               nome varchar(255) not null,
               sobrenome varchar(255) not null,
               email varchar(255) not null,
               endereco varchar(255) not null,
               telefone varchar(11) not null);""")

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS emprestimos
                   (id int auto_increment primary key,
                   id_livro int not null,
                   id_usuario int not null,
                   data_emprestimo varchar(10) not null,
                   data_devolucao varchar(10),
                   foreign key(id_livro) references livros(id),
                   foreign key(id_usuario) references usuarios(id)
                   );""")
            self.connection.commit()
        except Error as e:
            print(f"Erro enquanto cria tabela: {e}")

    #Adiciona livro ao banco de dados, pedindo, nessa ordem, Titulo,Autor e Editora
    def add_livro(self, Livro):
        self.cursor.execute("""SELECT COUNT(*) FROM livros WHERE titulo = %s AND autor = %s AND editora = %s AND categoria = %s""",
                            (Livro.titulo, Livro.autor, Livro.editora, Livro.categoria))
        count = self.cursor.fetchone()[0]

        if count == 0:
            self.cursor.execute("""INSERT INTO livros (titulo, autor, editora,categoria) VALUES (%s, %s, %s, %s)""",
                                (Livro.titulo, Livro.autor, Livro.editora, Livro.categoria))
            self.connection.commit()
            print(f"Livro '{Livro.titulo}' adicionado com sucesso!")
        else:
            print(f"Livro '{Livro.titulo}' já existe no banco de dados!")


    #Função que checa a existencia de um livro pelo titulo no banco de dados
    def checar_existencia(self,titulo):
        self.cursor.execute("""SELECT COUNT(*) FROM livros WHERE titulo like %s """,
                            (titulo,))
        count = self.cursor.fetchone()[0]
        if count != 0:
            print(f"Temos o livro: '{titulo}' na biblioteca!")
        else:
            print("Livro não encontrado!")

    #Função que adiciona usuário e se ja existir usuário no banco ele retorna "Já existente"
    def add_usuario(self, usuario):
        self.cursor.execute("""SELECT COUNT(*) FROM usuarios 
        WHERE nome = %s and sobrenome = %s """,
                            (usuario.nome, usuario.sobrenome))
        count = self.cursor.fetchone()[0]

        if count == 0:
            self.cursor.execute("""INSERT INTO usuarios(nome,sobrenome, email,endereco,telefone) 
            VALUES (%s, %s, %s, %s, %s)""",
                                (usuario.nome,usuario.sobrenome,usuario.email, usuario.endereco, usuario.telefone))
            self.connection.commit()
            print(f"Usuarios: '{usuario.nome}' adicionado com sucesso!")
        else:
            print(f"Usuario: '{usuario.nome}' já existe no banco de dados!")

    def listar_usuarios(self):
        self.cursor.execute("select id, nome,sobrenome,email,endereco from usuarios ")
        usuarios = self.cursor.fetchall()
        print("=" * 100)
        for usuario in usuarios:
            print(f"ID: {usuario[0]}|Nome: {usuario[1]}|Sobrenome: {usuario[2]}|Email: {usuario[3]}|Endereço: {usuario[4]} ")

    def filtrar_por_usuario(self, nome_usuario):
        a = 0
        self.cursor.execute("SELECT usuarios.id, usuarios.nome,usuarios.sobrenome, usuarios.email, usuarios.telefone, "
                            "usuarios.endereco "
                            "FROM usuarios "
                            "WHERE usuarios.nome like %s",
                            ("%{}%".format(nome_usuario),))

        resultado_pesquisa = self.cursor.fetchall()
        print("="*100)
        for usuario in resultado_pesquisa:
            a = 1
            print(f"ID:{usuario[0]} |Nome: {usuario[1]} |Sobrenome: {usuario[2]}|Email: {usuario[3]} "
                  f"|Telefone: {usuario[4]}|Endereço: {usuario[5]}")
        if a == 0:
            print("Não foi possivel encontrar esse usuario.")

    #Filtra por categoria e mostra em tela.
    #teste teste teste

    def filtrar_por_categorias(self, categoria):
        a = 0
        self.cursor.execute("SELECT livros.id, livros.titulo, livros.categoria, livros.autor FROM livros "
                            "WHERE livros.categoria like %s",
                            ("%{}%".format(categoria),))
        resultado_pesquisa = self.cursor.fetchall()
        print("="*100)
        for categorias in resultado_pesquisa:
            a = 1
            print(f"ID:{categorias[0]} |Titulo: {categorias[1]} |Categoria: {categorias[2]}|Autor: {categorias[3]}")
        if a == 0:
            print("Não foi possivel encontrar essa categoria.")

    def filtrar_por_autor(self, autor):
        a = 0
        self.cursor.execute("SELECT livros.id, livros.titulo,livros.autor, livros.categoria FROM livros "
                            "WHERE livros.autor like %s",
                            ("%{}%".format(autor),))
        resultado_pesquisa = self.cursor.fetchall()
        print("="*100)
        for autores in resultado_pesquisa:
            a = 1
            print(f"ID:{autores[0]} |Titulo: {autores[1]} |Autor: {autores[2]} |Categoria: {autores[3]} ")
        if a == 0:
            print("Não foi possivel encontrar essa autor.")

    def filtrar_por_titulo(self, titulo):
        a = 0
        self.cursor.execute("SELECT livros.id, livros.titulo,livros.autor, livros.categoria FROM livros "
                            "WHERE livros.titulo like %s",
                            ("%{}%".format(titulo),))
        resultado_pesquisa = self.cursor.fetchall()
        print("="*100)
        for titulos in resultado_pesquisa:
            a = 1
            print(f"ID:{titulos[0]} |Titulo: {titulos[1]} |Autor: {titulos[2]} |Categoria: {titulos[3]} ")
        if a == 0:
            print("Não foi possivel encontrar essa titulo.")

    def listar_livros(self):
        self.cursor.execute("select livros.id, livros.titulo, livros.autor, livros.categoria from livros")
        resultado_pesquisa = self.cursor.fetchall()
        print("=" * 100)
        for livros in resultado_pesquisa:
            print(f"ID: {livros[0]} |Titulo: {livros[1]} |Autor: {livros[2]} | Categoria: {livros[3]}")
            print("=" * 100)

    def emprestar_livro(self, id_livro, id_usuario, data_emprestimo, data_devolucao):
        self.cursor.execute("SELECT COUNT(*) FROM emprestimos WHERE id_livro = %s AND data_devolucao IS NULL",
                            (id_livro,))
        resultado = self.cursor.fetchone()

        if resultado[0] == 0:
            print("=" * 100)
            self.cursor.execute(
                "INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) "
                "VALUES (%s, %s, %s, %s)",
                (id_livro, id_usuario, data_emprestimo, data_devolucao))
            print("Empréstimo realizado com sucesso.")
        else:
            print("="*100)
            print(f"Este livro já está emprestado e não pode ser \n"
                  f"emprestado novamente até que seja devolvido.")
        self.connection.commit()

    def exibir_emprestados(self):
        a = 0
        self.cursor.execute("SELECT livros.id, livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, "
                            "emprestimos.data_devolucao FROM livros "
                            "INNER JOIN emprestimos ON livros.id = emprestimos.id_livro "
                            "INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario "
                            "WHERE emprestimos.data_devolucao IS NULL")
        resultados = self.cursor.fetchall()
        print("=" *100)
        for resultado in resultados:
            a = 1
            print(f"ID:{resultado[0]}")
            print(f"Nome: {resultado[2]} {resultado[3]}")
            print(f"Livro: {resultado[1]}")
            print(f"Data do empréstimo: {resultado[4]}")
            if resultado[5] is None:
                print("Ainda não devolvido.")
            else:
                print("Devolvido.")
        if a == 0:
            print("Nenhum empréstimo realizado ainda.")

    def inserir_data_devolucao(self, id_livro, data_devolucao):
        self.cursor.execute("""UPDATE emprestimos SET data_devolucao = %s WHERE id_livro = %s"""
                            , (data_devolucao, id_livro))
        self.connection.commit()
        print("Devolução realizada com sucesso!")



    # Desconecta do banco de dados
    def close_connection(self):
        try:
            if self.connection and self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
        except AttributeError:
            pass




db = Database()
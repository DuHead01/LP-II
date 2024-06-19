class Livro:
    def __init__(self, titulo, autor, editora, categoria):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.categoria = categoria

    def toString(self):
        return (f"Livro[ Titulo: {self.titulo}, Autor: {self.autor}, Editora: {self.editora}, "
                f"Categoria:{self.categoria} ] ")

    def get_titulo(self):
        return self.titulo
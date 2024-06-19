class Usuario:
    cadastroUsuarioAtual = 1

    def __init__(self, nome, sobrenome, email, endereco, telefone):
        self.cadastroUsuario = Usuario.cadastroUsuarioAtual
        Usuario.cadastroUsuarioAtual += 1
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

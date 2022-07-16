class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property # retorna um valor
    def nome(self):
        return self._nome
    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1

    @nome.setter #dar um novo valor
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    @property
    def get_like(self):
        return self._like

    def imprime(self):
        print(f"{self.nome} - {self.ano} - {self.like} Likes")

class Filme(Programa):
    def __init__(self, nome, duracao, ano):
        super().__init__(nome, ano)
        self.duracao = duracao
    def imprime(self):
        print(f"{self.nome} - {self.ano} - {self.duracao} min - {self.like} Likes")

class Serie(Programa):
    def __init__(self, nome, temporadas, ano):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def imprime(self):
        print(f"{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.like} Likes")


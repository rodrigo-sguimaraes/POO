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

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.like} Likes"

class Filme(Programa):
    def __init__(self, nome, duracao, ano):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} min - {self.like} Likes"

class Serie(Programa):
    def __init__(self, nome, temporadas, ano):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.like} Likes"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)
vingadores = Filme("Vingadores - Guerra Infinita", 216, 2018)
tmep = Filme("Todo mundo em panico", 1999, 100)
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()

atlanta = Serie("Atlanta", 2, 2016)
suits = Serie("Suits", 7, 2018)
atlanta.dar_like()
atlanta.dar_like()
suits.dar_like()
suits.dar_like()
suits.dar_like()

filmes_e_series = [vingadores, atlanta, tmep, suits]
playlist_fim_de_semana = Playlist('Filmes e Séries', filmes_e_series)

print(f'O tamanho de minha playlist é: {len(playlist_fim_de_semana)}')
for programa in playlist_fim_de_semana:
    print(programa)


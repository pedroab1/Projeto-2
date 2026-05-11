class Musica:
    def __init__(self, id, titulo, artista, genero, bpm):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def exibir_dados(self):
        print(f"ID: {self.id}")
        print(f"Título: {self.titulo}")
        print(f"Artista: {self.artista}")
        print(f"Gênero: {self.genero}")
        print(f"BPM: {self.bpm}")
        print("-" * 30)

        #exemplo de uso
musica1 = Musica(1, "Silver Linings", "Piphoka", "Lo-fi", 92)
musica1.exibir_dados()
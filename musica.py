class Musica:
    def __init__(self, id, titulo, artista, genero, bpm):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def __str__(self) -> str:
        return (
            f"[ID: {self.id}] {self.titulo} — {self.artista} "
            f"| Gênero: {self.genero} | BPM: {self.bpm}"
        )

    def __repr__(self) -> str:
        return (
            f"Musica(id={self.id!r}, titulo={self.titulo!r}, "
            f"artista={self.artista!r}, genero={self.genero!r}, bpm={self.bpm!r})"
        )
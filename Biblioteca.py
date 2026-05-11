from musica import Musica
from nodo_lista import NodoLista

class Biblioteca:
    def __init__(self):
        self.inicio = None
        self.proximo_id = 1

    def adicionar_musica(self, titulo, artista, genero, bpm):
        # O nome da classe deve ser Musica (com M maiúsculo)
        nova_musica = Musica(
            self.proximo_id,
            titulo,
            artista,
            genero,
            bpm
        )

        # O nome da classe deve ser NodoLista (com N e L maiúsculos)
        novo_nodo = NodoLista(nova_musica)

        # Lista vazia
        if self.inicio is None:
            self.inicio = novo_nodo

        # Inserção no final
        else:
            atual = self.inicio

            while atual.proximo is not None:
                atual = atual.proximo

            atual.proximo = novo_nodo

        print("Música adicionada com sucesso!")

        self.proximo_id += 1

    def remover_musica(self, id):
        if self.inicio is None:
            print("Biblioteca vazia.")
            return

        atual = self.inicio
        anterior = None

        while atual is not None:
            # Música encontrada
            if atual.musica.id == id:
                # Remover primeiro nó
                if anterior is None:
                    self.inicio = atual.proximo
                # Remover nó do meio/final
                else:
                    anterior.proximo = atual.proximo

                print("Música removida com sucesso!")
                return

            anterior = atual
            atual = atual.proximo

        print("ID não encontrado.")

    def buscar_por_id(self, id):
        atual = self.inicio
        while atual is not None:
            if atual.musica.id == id:
                atual.musica.exibir_dados()
                return atual.musica
            atual = atual.proximo

        print("Música não encontrada.")
        return None

    def buscar_por_titulo(self, titulo):
        atual = self.inicio
        while atual is not None:
            if atual.musica.titulo.lower() == titulo.lower():
                atual.musica.exibir_dados()
                return atual.musica
            atual = atual.proximo

        print("Música não encontrada.")
        return None

    def listar_musicas(self):
        if self.inicio is None:
            print("Biblioteca vazia.")
            return

        atual = self.inicio
        while atual is not None:
            atual.musica.exibir_dados()
            atual = atual.proximo
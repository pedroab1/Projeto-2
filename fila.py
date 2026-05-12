from nodo_fila import NodoFila

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def enqueue(self, musica):
        novo_nodo = NodoFila(musica)

        if self.esta_vazia():
            self.inicio = novo_nodo
            self.fim = novo_nodo

        else:
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo

        self.tamanho += 1

    def dequeue(self):
        if self.esta_vazia():
            return None

        musica_removida = self.inicio.musica

        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        self.tamanho -= 1

        return musica_removida

    def exibir_fila(self):
        if self.esta_vazia():
            print("Fila vazia.")
            return

        atual = self.inicio

        while atual is not None:
            atual.musica.exibir_dados()
            atual = atual.proximo
from nodo_fila import NodoFila

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def enqueue(self, musica):
        # O nome da classe deve ser NodoFila (com N e F maiúsculos)
        novo_nodo = NodoFila(musica)

        # Se a fila estiver vazia
        if self.esta_vazia():
            self.inicio = novo_nodo
            self.fim = novo_nodo

        # Inserção no final
        else:
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo

        self.tamanho += 1

    def dequeue(self):
        # Fila vazia
        if self.esta_vazia():
            return None

        musica_removida = self.inicio.musica

        self.inicio = self.inicio.proximo

        # Se a fila ficou vazia
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
            # O método exibir_dados() pertence à classe Musica
            atual.musica.exibir_dados()
            atual = atual.proximo
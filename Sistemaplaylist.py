from Biblioteca import Biblioteca
from fila import Fila

class SistemaPlaylist:
    def __init__(self):
        self.biblioteca = Biblioteca()

        self.fila_relaxar = Fila()
        self.fila_focar = Fila()
        self.fila_animar = Fila()
        self.fila_treinar = Fila()

        self.historico = Fila()

    def limpar_fila(self, fila):
        while not fila.esta_vazia():
            fila.dequeue()

    def montar_filas_humor(self):
        self.limpar_fila(self.fila_relaxar)
        self.limpar_fila(self.fila_focar)
        self.limpar_fila(self.fila_animar)
        self.limpar_fila(self.fila_treinar)

        atual = self.biblioteca.inicio

        while atual is not None:
            musica = atual.musica
            bpm = musica.bpm

            if bpm <= 80:
                self.fila_relaxar.enqueue(musica)
            elif bpm <= 120:
                self.fila_focar.enqueue(musica)
            elif bpm <= 160:
                self.fila_animar.enqueue(musica)
            else:
                self.fila_treinar.enqueue(musica)

            atual = atual.proximo

        print("Filas de humor montadas com sucesso!")

    def reproduzir_proxima(self, humor):
        if humor == "relaxar":
            musica = self.fila_relaxar.dequeue()
        elif humor == "focar":
            musica = self.fila_focar.dequeue()
        elif humor == "animar":
            musica = self.fila_animar.dequeue()
        elif humor == "treinar":
            musica = self.fila_treinar.dequeue()
        else:
            print("Humor inválido.")
            return

        if musica is None:
            print("Fila vazia.")
            return

        print("Reproduzindo agora:")
        musica.exibir_dados()

        
        self.historico.enqueue(musica)

    def exibir_fila_humor(self, humor):
        if humor == "relaxar":
            self.fila_relaxar.exibir_fila()
        elif humor == "focar":
            self.fila_focar.exibir_fila()
        elif humor == "animar":
            self.fila_animar.exibir_fila()
        elif humor == "treinar":
            self.fila_treinar.exibir_fila()
        else:
            print("Humor inválido.")

    def exibir_historico(self):
        print("Histórico de reproduções:")
        self.historico.exibir_fila()

    def estatisticas(self):
        total_biblioteca = 0
        atual = self.biblioteca.inicio

        while atual is not None:
            total_biblioteca += 1
            atual = atual.proximo

        print("\n===== ESTATÍSTICAS =====")
        print(f"Total na biblioteca: {total_biblioteca}")
        print(f"Fila Relaxar: {self.fila_relaxar.tamanho}")
        print(f"Fila Focar: {self.fila_focar.tamanho}")
        print(f"Fila Animar: {self.fila_animar.tamanho}")
        print(f"Fila Treinar: {self.fila_treinar.tamanho}")
        print(f"Músicas reproduzidas: {self.historico.tamanho}")


sistema = SistemaPlaylist()

while True:
    print("\n===== SISTEMA PLAYLIST =====")
    print("1 - Adicionar música")
    print("2 - Remover música")
    print("3 - Buscar música por ID")
    print("4 - Buscar música por título")
    print("5 - Listar biblioteca")
    print("6 - Montar filas de humor")
    print("7 - Reproduzir próxima música")
    print("8 - Exibir fila de humor")
    print("9 - Exibir histórico")
    print("10 - Estatísticas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        artista = input("Artista: ")
        genero = input("Gênero: ")
        try:
            bpm = int(input("BPM: "))
            if bpm <= 0:
                print("BPM deve ser maior que zero.")
                continue
            sistema.biblioteca.adicionar_musica(titulo, artista, genero, bpm)
        except ValueError:
            print("Digite um BPM numérico.")

    elif opcao == "2":
        try:
            id_busca = int(input("Digite o ID da música: "))
            sistema.biblioteca.remover_musica(id_busca)
        except ValueError:
            print("Digite um ID válido.")

    elif opcao == "3":
        try:
            id_busca = int(input("Digite o ID da música: "))
            sistema.biblioteca.buscar_por_id(id_busca)
        except ValueError:
            print("Digite um ID válido.")

    elif opcao == "4":
        titulo = input("Digite o título: ")
        sistema.biblioteca.buscar_por_titulo(titulo)

    elif opcao == "5":
        sistema.biblioteca.listar_musicas()

    elif opcao == "6":
        sistema.montar_filas_humor()

    elif opcao == "7":
        print("\nHumores: relaxar, focar, animar, treinar")
        humor = input("Escolha a fila: ").lower()
        sistema.reproduzir_proxima(humor)

    elif opcao == "8":
        print("\nHumores: relaxar, focar, animar, treinar")
        humor = input("Escolha a fila: ").lower()
        sistema.exibir_fila_humor(humor)

    elif opcao == "9":
        sistema.exibir_historico()

    elif opcao == "10":
        sistema.estatisticas()

    elif opcao == "0":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida.")
class Musica:
    def __init__(self, id_musica, titulo, artista, genero, bpm):
        self.id = id_musica
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None

class NodoFila:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None



class Biblioteca:
    def __init__(self):
        self.inicio = None
        self.contador_id = 1
        self.total_musicas = 0

    def adicionar(self, titulo, artista, genero, bpm):
        nova_musica = Musica(self.contador_id, titulo, artista, genero, bpm)
        self.contador_id += 1
        novo_nodo = NodoLista(nova_musica)

        if self.inicio is None:
            self.inicio = novo_nodo
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo
        
        self.total_musicas += 1
        print(f"\n[+] Música '{titulo}' adicionada com sucesso! (ID: {nova_musica.id})")

    def remover(self, id_busca):
        if self.inicio is None:
            print("\n[-] A biblioteca está vazia.")
            return False

        
        if self.inicio.musica.id == id_busca:
            print(f"\n[-] Música '{self.inicio.musica.titulo}' removida.")
            self.inicio = self.inicio.proximo
            self.total_musicas -= 1
            return True

        
        atual = self.inicio
        while atual.proximo is not None:
            if atual.proximo.musica.id == id_busca:
                print(f"\n[-] Música '{atual.proximo.musica.titulo}' removida.")
                atual.proximo = atual.proximo.proximo
                self.total_musicas -= 1
                return True
            atual = atual.proximo

        print("\n[!] ID inexistente na biblioteca.")
        return False

    def buscar(self, termo):
        if self.inicio is None:
            print("\n[-] A biblioteca está vazia.")
            return

        atual = self.inicio
        encontrou = False
        
        try:
            termo_id = int(termo)
        except ValueError:
            termo_id = -1

        while atual is not None:
            m = atual.musica
            if m.id == termo_id or m.titulo.lower() == str(termo).lower():
                print(f"\n=> ID: {m.id} | {m.titulo} - {m.artista} ({m.genero}) | BPM: {m.bpm}")
                encontrou = True
            atual = atual.proximo
        
        if not encontrou:
            print("\n[!] Nenhuma música encontrada com esse ID ou Título.")

    def listar(self):
        if self.inicio is None:
            print("\n[-] A biblioteca está vazia.")
            return

        print("\n--- BIBLIOTECA COMPLETA ---")
        atual = self.inicio
        while atual is not None:
            m = atual.musica
            print(f"ID: {m.id} | {m.titulo} - {m.artista} | BPM: {m.bpm}")
            atual = atual.proximo



class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enqueue(self, musica):
        novo_nodo = NodoFila(musica)
        if self.fim is None:
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo
        self.tamanho += 1

    def dequeue(self):
        if self.inicio is None:
            return None
        
        musica_removida = self.inicio.musica
        self.inicio = self.inicio.proximo
        
        if self.inicio is None:
            self.fim = None
            
        self.tamanho -= 1
        return musica_removida

    def limpar(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def listar_fila(self):
        if self.inicio is None:
            print("Fila vazia.")
            return

        atual = self.inicio
        posicao = 1
        while atual is not None:
            print(f"{posicao}º -> {atual.musica.titulo} ({atual.musica.bpm} BPM)")
            atual = atual.proximo
            posicao += 1



def main():
    biblio = Biblioteca()
    fila_relaxar = Fila()
    fila_focar = Fila()
    fila_animar = Fila()
    fila_treinar = Fila()
    historico = Fila()

    while True:
        print("\n" + "="*30)
        print(" SISTEMA DE PLAYLIST ")
        print("="*30)
        print("1. Adicionar música à biblioteca")
        print("2. Remover música da biblioteca")
        print("3. Buscar música")
        print("4. Listar biblioteca completa")
        print("5. Montar fila de reprodução por humor")
        print("6. Reproduzir próxima")
        print("7. Exibir fila de humor")
        print("8. Exibir histórico de reproduções")
        print("9. Estatísticas")
        print("10. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título: ")
            artista = input("Artista: ")
            genero = input("Gênero: ")
            bpm_input = input("BPM: ")
            
            
            try:
                bpm = int(bpm_input)
                if bpm <= 0:
                    print("\n[!] O BPM deve ser maior que zero!")
                else:
                    biblio.adicionar(titulo, artista, genero, bpm)
            except ValueError:
                print("\n[!] Erro: BPM não numérico. Digite um número inteiro.")

        elif opcao == '2':
            try:
                id_rem = int(input("Digite o ID da música para remover: "))
                biblio.remover(id_rem)
            except ValueError:
                print("\n[!] Digite um ID numérico válido.")

        elif opcao == '3':
            termo = input("Digite o ID ou Título da música: ")
            biblio.buscar(termo)

        elif opcao == '4':
            biblio.listar()

        elif opcao == '5':
            
            fila_relaxar.limpar()
            fila_focar.limpar()
            fila_animar.limpar()
            fila_treinar.limpar()

            
            atual = biblio.inicio
            while atual is not None:
                m = atual.musica
                if m.bpm <= 80:
                    fila_relaxar.enqueue(m)
                elif 81 <= m.bpm <= 120:
                    fila_focar.enqueue(m)
                elif 121 <= m.bpm <= 160:
                    fila_animar.enqueue(m)
                else: 
                    fila_treinar.enqueue(m)
                atual = atual.proximo
            
            print("\n[+] Filas de humor montadas com sucesso baseadas na biblioteca atual!")

        elif opcao == '6':
            print("\nQual fila deseja reproduzir?")
            print("1. Relaxar | 2. Focar | 3. Animar | 4. Treinar")
            esc = input("Escolha (1-4): ")
            
            musica_tocada = None
            if esc == '1': musica_tocada = fila_relaxar.dequeue()
            elif esc == '2': musica_tocada = fila_focar.dequeue()
            elif esc == '3': musica_tocada = fila_animar.dequeue()
            elif esc == '4': musica_tocada = fila_treinar.dequeue()
            else:
                print("\n[!] Opção de fila inválida.")
                continue

            if musica_tocada is None:
                print("\n[!] A fila escolhida está vazia! Não há músicas para reproduzir.")
            else:
                print(f"\n TOCANDO AGORA: {musica_tocada.titulo} - {musica_tocada.artista}")
                historico.enqueue(musica_tocada) 

        elif opcao == '7':
            print("\nQual fila deseja exibir?")
            print("1. Relaxar | 2. Focar | 3. Animar | 4. Treinar")
            esc = input("Escolha (1-4): ")
            
            print("\n--- FILA SELECIONADA ---")
            if esc == '1': fila_relaxar.listar_fila()
            elif esc == '2': fila_focar.listar_fila()
            elif esc == '3': fila_animar.listar_fila()
            elif esc == '4': fila_treinar.listar_fila()
            else: print("\n[!] Opção de fila inválida.")

        elif opcao == '8':
            print("\n--- HISTÓRICO DE REPRODUÇÕES ---")
            historico.listar_fila()

        elif opcao == '9':
            print("\n--- ESTATÍSTICAS ---")
            print(f"Músicas na Biblioteca: {biblio.total_musicas}")
            print(f"Fila Relaxar (<= 80): {fila_relaxar.tamanho} músicas")
            print(f"Fila Focar (81-120): {fila_focar.tamanho} músicas")
            print(f"Fila Animar (121-160): {fila_animar.tamanho} músicas")
            print(f"Fila Treinar (> 160): {fila_treinar.tamanho} músicas")
            print(f"Total já reproduzidas: {historico.tamanho} músicas")

        elif opcao == '10':
            print("\nSaindo... Valeu!")
            break
        else:
            print("\n[!] Opção inválida do menu.")

if __name__ == "__main__":
    main()
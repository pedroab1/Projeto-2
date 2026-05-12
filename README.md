# Sistema de Gerenciamento de Playlist - Projeto 2

Este projeto consiste no desenvolvimento do backend de um sistema de gerenciamento de músicas, focado na implementação manual de estruturas de dados fundamentais. O software permite organizar uma biblioteca pessoal, categorizar faixas por "humor" (BPM) e manter um histórico de reprodução.

## Objetivo
O objetivo principal é gerenciar uma biblioteca musical utilizando estritamente **Listas Encadeadas** e **Filas FIFO** implementadas do zero, sem o auxílio de coleções nativas do Python (como `list`, `deque` ou `dict`).

## Requisitos Técnicos
Para cumprir os requisitos técnicos da disciplina, foram implementadas as seguintes classes:
* **Musica**: Representa uma faixa contendo `id`, `titulo`, `artista`, `genero` e `bpm`.
* **NodoLista / NodoFila**: Estruturas de nós para apontamento em memória.
* **Biblioteca (Lista Encadeada)**: Armazena todas as músicas cadastradas e permite inserção, remoção e busca.
* **Fila (FIFO)**: Implementação própria com `enqueue` e `dequeue` para as filas de humor e o histórico.
* **ID Sequencial**: Gerado automaticamente e não reutilizado após a remoção de uma faixa.

## Funcionalidades
O sistema oferece um menu interativo com as seguintes opções:
1.  **Adicionar música**: Insere no final da lista, solicitando título, artista, gênero e BPM com validação.
2.  **Remover música**: Busca pelo ID e remove o nó correspondente da lista encadeada.
3.  **Buscar música**: Permite a pesquisa por ID ou por Título, exibindo os dados da faixa encontrada.
4.  **Listar biblioteca**: Percorre a lista encadeada do início ao fim para exibir todas as músicas.
5.  **Montar filas por humor**: Classifica automaticamente as músicas baseadas no BPM. Esta operação limpa as filas anteriores antes de remontá-las.
6.  **Reproduzir próxima**: Retira a música do topo da fila de humor escolhida, exibe seus dados e a enfileira no histórico.
7.  **Exibir fila de humor**: Mostra todas as músicas em espera em uma categoria sem removê-las.
8.  **Exibir histórico**: Lista todas as músicas já reproduzidas em ordem cronológica.
9.  **Estatísticas**: Exibe o total na biblioteca, o tamanho de cada fila de humor e o total de músicas reproduzidas.

## Classificação por Humor (BPM)
A organização das filas segue os critérios técnicos definidos para o projeto:

| Fila | Humor | Faixa de BPM |
| :--- | :--- | :--- |
| **Relaxar** | Tranquilo | Até 80 BPM |
| **Focar** | Concentração | 81 a 120 BPM |
| **Animar** | Agitado | 121 a 160 BPM |
| **Treinar** | Intenso | Acima de 160 BPM |

## Como Executar
1. Certifique-se de ter o Python 3 instalado.
2. Certifique-se de que todos os arquivos `.py` estão no mesmo diretório.
3. Execute o comando:
   ```bash
   python Sistemaplaylist.py
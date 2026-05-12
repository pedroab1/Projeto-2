# Sistema de Gerenciamento de Playlist - Estrutura de Dados

[cite_start]Este projeto consiste no desenvolvimento do backend de um sistema de gerenciamento de músicas, focado na implementação manual de estruturas de dados fundamentais[cite: 4, 5]. [cite_start]O software permite organizar uma biblioteca pessoal, categorizar faixas por "humor" (BPM) e manter um histórico de reprodução[cite: 5, 6].


## 🎯 Objetivo
[cite_start]O objetivo principal é gerenciar uma biblioteca musical utilizando estritamente **Listas Encadeadas** e **Filas FIFO** implementadas do zero, sem o auxílio de coleções nativas do Python (como `list`, `deque` ou `dict`)[cite: 43].


## 🛠️ Requisitos Técnicos
Para cumprir os requisitos técnicos da disciplina, foram implementadas as seguintes classes:
* [cite_start]**Musica**: Representa uma faixa contendo `id`, `titulo`, `artista`, `genero` e `bpm`[cite: 8].
* [cite_start]**NodoLista / NodoFila**: Estruturas de nós para apontamento em memória[cite: 9, 11].
* [cite_start]**Biblioteca (Lista Encadeada)**: Armazena todas as músicas cadastradas e permite inserção, remoção e busca[cite: 10].
* [cite_start]**Fila (FIFO)**: Implementação própria com `enqueue` e `dequeue` para as filas de humor e o histórico[cite: 13, 14, 44].
* [cite_start]**ID Sequencial**: Gerado automaticamente e não reutilizado após a remoção de uma faixa[cite: 18, 47].



## 🚀 Funcionalidades
O sistema oferece um menu interativo com as seguintes opções:
1.  [cite_start]**Adicionar música**: Insere no final da lista, solicitando título, artista, gênero e BPM com validação[cite: 16, 17, 18, 48].
2.  [cite_start]**Remover música**: Busca pelo ID e remove o nó correspondente da lista encadeada[cite: 19, 20].
3.  [cite_start]**Buscar música**: Permite a pesquisa por ID ou por Título, exibindo os dados da faixa encontrada[cite: 22].
4.  [cite_start]**Listar biblioteca**: Percorre a lista encadeada do início ao fim para exibir todas as músicas[cite: 23, 25].
5.  **Montar filas por humor**: Classifica automaticamente as músicas baseadas no BPM. [cite_start]Esta operação limpa as filas anteriores antes de remontá-las[cite: 27, 45, 46].
6.  [cite_start]**Reproduzir próxima**: Retira a música do topo da fila de humor escolhida, exibe seus dados e a enfileira no histórico[cite: 31, 32].
7.  [cite_start]**Exibir fila de humor**: Mostra todas as músicas em espera em uma categoria sem removê-las[cite: 33, 34].
8.  [cite_start]**Exibir histórico**: Lista todas as músicas já reproduzidas em ordem cronológica[cite: 36, 38].
9.  [cite_start]**Estatísticas**: Exibe o total na biblioteca, o tamanho de cada fila de humor e o total de músicas reproduzidas[cite: 39, 40].



## 🎼 Classificação por Humor (BPM)
[cite_start]A organização das filas segue os critérios técnicos definidos para o projeto[cite: 29]:

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


# Sistema de Playlist - Estrutura de Dados
Este projeto consiste no desenvolvimento do backend de um sistema de gerenciamento de músicas, focado na implementação manual de estruturas de dados fundamentais. O projeto foi desenvolvido para a disciplina de **Estrutura de Dados** na **Fatec Rio Claro**.

## Objetivo do Projeto
O objetivo principal é gerenciar uma biblioteca musical e organizar filas de reprodução baseadas no "humor" (BPM) das faixas, utilizando estritamente **Listas Encadeadas** e **Filas FIFO** implementadas do zero, sem o auxílio de coleções nativas do Python (como `list`, `deque` ou `dict`).

## Estruturas de Dados Utilizadas
Para cumprir os requisitos técnicos, foram implementadas as seguintes classes:
- **Musica**: Objeto contendo `id`, `titulo`, `artista`, `genero` e `bpm`.
- **NodoLista / NodoFila**: Estruturas de nós para apontamento em memória.
- **Biblioteca (Lista Encadeada)**: Armazena todas as músicas cadastradas.
- **Fila (FIFO)**: Gerencia as 4 filas de humor e a fila de histórico de reprodução.

## Funcionalidades
O sistema oferece um menu interativo com as seguintes opções:
1.  **Adicionar música**: Cadastro com ID sequencial automático e validação de BPM.
2.  **Remover música**: Busca e exclusão por ID.
3.  **Buscar música**: Pesquisa por ID ou Título.
4.  **Listar biblioteca**: Exibição completa de todas as faixas.
5.  **Montar filas por humor**: Classificação automática baseada no BPM:
    - **Relaxar**: até 80 BPM.
    - **Focar**: de 81 a 120 BPM.
    - **Animar**: de 121 a 160 BPM.
    - **Treinar**: acima de 160 BPM.
6.  **Reproduzir próxima**: Retira a música da fila escolhida e envia para o Histórico.
7.  **Exibir fila**: Visualização das faixas em espera em cada categoria.
8.  **Histórico**: Lista todas as músicas já reproduzidas.
9.  **Estatísticas**: Exibe o total de músicas na biblioteca e o tamanho de cada fila.

## Como Executar
Certifique-se de ter o Python 3 instalado.
1. Clone o repositório.
2. Navegue até a pasta do projeto.
3. Execute o comando:
   ```bash
   python main.py

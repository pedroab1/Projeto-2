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

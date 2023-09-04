# Competitive Code

Este repositório contém código para programação competitiva. O objetivo deste código é fornecer funções úteis para a resolução de problemas em competições de programação. Ele inclui funcionalidades para contar o número de inputs em um arquivo de código e contar o número total de elementos em um arquivo de entrada.

## Funcionalidades

O arquivo `competitive_code.py` contém as seguintes funções:

- `count_inputs(filename)`: Esta função recebe o nome de um arquivo de código como parâmetro e retorna o número de inputs encontrados no arquivo. Ela realiza uma busca por ocorrências da função `input()` no código e conta quantas vezes ela aparece.

- `count_elements(input_file)`: Esta função recebe o caminho de um arquivo de entrada como parâmetro e conta o número total de elementos presentes no arquivo. Ela lê o arquivo de entrada, que contém linhas de inputs separadas por quebras de linha, e conta quantos elementos existem em cada linha.

- `main()`: Esta é a função principal do código. Ela lê as entradas do arquivo de entrada, executa o código e salva a saída múltiplas vezes. A função `main()` recebe como parâmetros o caminho do arquivo de código, o caminho do arquivo de entrada e o caminho do arquivo de saída. Ela utiliza as funções `count_inputs()` e `count_elements()` para obter informações sobre o número de inputs e elementos, respectivamente. Em seguida, ela itera sobre as linhas de inputs do arquivo de entrada, executa o código com cada conjunto de inputs e salva a saída no arquivo de saída.

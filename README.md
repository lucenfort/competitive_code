# Competitive Code

Este repositório contém código para programação competitiva. O objetivo deste código é fornecer funções úteis para a resolução de problemas em competições de programação. Ele inclui funcionalidades para contar o número de inputs em um arquivo de código e contar o número total de elementos em um arquivo de entrada.

## Funcionalidades

O arquivo `competitive_code.py` contém as seguintes funções:

- `count_inputs(filename)`: Esta função recebe o nome de um arquivo de código como parâmetro e retorna o número de inputs encontrados no arquivo. Ela realiza uma busca por ocorrências da função `input()` no código e conta quantas vezes ela aparece.

- `count_elements(input_file)`: Esta função recebe o caminho de um arquivo de entrada como parâmetro e conta o número total de elementos presentes no arquivo. Ela lê o arquivo de entrada, que contém linhas de inputs separadas por quebras de linha, e conta quantos elementos existem em cada linha.

- `main()`: Esta é a função principal do código. Ela lê as entradas do arquivo de entrada, executa o código e salva a saída múltiplas vezes. A função `main()` recebe como parâmetros o caminho do arquivo de código, o caminho do arquivo de entrada e o caminho do arquivo de saída. Ela utiliza as funções `count_inputs()` e `count_elements()` para obter informações sobre o número de inputs e elementos, respectivamente. Em seguida, ela itera sobre as linhas de inputs do arquivo de entrada, executa o código com cada conjunto de inputs e salva a saída no arquivo de saída.

## Instalação

Para utilizar este código, siga as instruções abaixo:

1. Clone o repositório para o seu ambiente local:
```
git clone https://github.com/your-username/competitive-code.git
```

2. Certifique-se de ter as dependências necessárias instaladas.

## Uso

Para utilizar o código, siga as etapas abaixo:

1. Abra o arquivo `competitive_code.py` em um editor de texto.

2. Na função `main()`, defina os caminhos para o arquivo de código, o arquivo de entrada e o arquivo de saída. Certifique-se de que os arquivos existam no caminho especificado.

3. Personalize a lógica de execução do código, se necessário. Você pode adicionar ou modificar os comandos dentro do bloco `for` na função `main()` para adaptar o código às suas necessidades.

4. O código irá ler as entradas do arquivo de entrada, executar o código com cada conjunto de inputs e salvar a saída no arquivo de saída.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma sugestão de melhoria, sinta-se à vontade para enviar uma pull request. Antes de contribuir, leia as [diretrizes de contribuição](CONTRIBUTING.md) para obter mais informações.

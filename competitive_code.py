import os
import cProfile
import subprocess

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def count_inputs(filename):
    """
    Retorna o número de inputs encontrados em um arquivo de código.

    Parameters:
    filename (str): O nome do arquivo de código.

    Returns:
    int: O número de inputs encontrados no arquivo de código.
    """

    contador_inputs = 0

    with open(filename, "r") as arquivo:
        for linha in arquivo:
            if "input(" in linha:
                contador_inputs += 1

    return contador_inputs

def count_elements(input_file):
    """
    Conta o número total de elementos no arquivo de entrada.

    Args:
        input_file (str): O caminho do arquivo de entrada.

    Returns:
        int: O número total de elementos no arquivo de entrada.
    """

    with open(input_file, "r", encoding="utf-8") as f:
        inputs = f.read().splitlines()

    total_elements = 0
    for input_line in inputs:
        elements = input_line.split()
        total_elements += len(elements)

    return total_elements

def main():
    """
    Função principal que lê as entradas, executa o código e salva a saída N vezes.

    Args:
        code_file (str): O nome do arquivo de código.
        input_file (str): O caminho do arquivo de entrada.
        output_file (str): O caminho do arquivo de saída.
        
    Returns:
        None
    """
    clear_console() # Limpa console
    
    # Defina os caminhos dos arquivos de entrada, saída e do código a ser executado
    code_file = "calcular_preço_final_do_pedido.py"
    input_file = "data/input.txt"
    output_file = "data/output.txt"

    # Obter o número de inputs e elementos
    print("\n====================================================")
    num_inputs = count_inputs(code_file)
    num_elements = count_elements(input_file)
    print(f"INPUTS.:\t{num_inputs}\nELEMENTOS.:\t{num_elements}")
    print("====================================================\n")

    # Leitura das entradas do arquivo de entrada
    with open(input_file, "r", encoding="utf-8") as f:
        inputs = f.read().splitlines()

    num_executions = 0  # Counter variable for number of executions

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for i in range(0, num_elements,  num_inputs):
                print(">>>\t", end="")
                chunk = inputs[i:i+ num_inputs]  # Take N elements from the input file
                num_executions += 1  # Increment the counter for each execution

                # Execução do arquivo.py
                completed_process = subprocess.run(["python", code_file], input="\n".join(chunk), text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                # Verificar se a execução foi bem-sucedida
                if completed_process.returncode == 0:
                    process_output = completed_process.stdout

                    # Verificar se há saída do processo
                    if process_output:
                        # Imprimir a saída
                        print(process_output)

                        # Salvamento da saída no arquivo de saída
                        f.write(process_output)
                    else:
                        print("Nenhuma saída foi recebida do processo.")
                else:
                    print(f"@@@ Erro ao executar {code_file} @@@")

    except subprocess.CalledProcessError as e:
        print(f"@@@ Erro ao executar {code_file} @@@\n\t<erro:>", e)

    # Print the number of executions
    print(">>> Número de execuções realizadas:", num_executions, end="\n\n")

if __name__ == "__main__":
    cProfile.run("main()")

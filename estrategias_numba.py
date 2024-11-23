import time
import numpy as np
import main
from rich.console import Console
from rich.table import Table
from numba import jit

# -------------------------------------------------------------------------------------------------------------------- #

# Função para calcular o custo benefício de cada item dentro da mochila, sendo
# chamada no começo do algoritmo guloso para determinar todos os custos estabelecidos 
@jit(nopython=True)
def calcular_custo_beneficio(custo, beneficio, tam):
    custoBenef = []
    
    for i in range(tam): # 2n + 2
        
        if custo[i] == 0: # 2n
            custoBenef.append((beneficio[i]/(custo[i]+1), custo[i], i))  # 6n
        else:
            custoBenef.append((beneficio[i]/custo[i], custo[i], i)) # 5n
            
    return custoBenef

# Função que seleciona os itens para colocar na mochila com base no custo benefício
# feito anteriormente pela outra função
@jit(nopython=True)
def selecionar_itens(custoBenef, pesoMax, tam):
    
    armazenado = []
    presente = set() # 1
    
    # Percorre todos os itens que entrarament
    for i in range(tam): # 2n + 2
        
        # Inicializa a variável de maior custo benefício
        maior = -999999 # n
        
        for j in range(tam): # n (2n + 2) = 2n^2 + 2n
            if custoBenef[j][0] > maior and j not in presente: # 10n^2 + 10n
                maior = custoBenef[j][0] # 6n^2 + 6n
                pos = j # 2n^2 + 2n
                
        if custoBenef[pos][1] <= pesoMax: # 3n
            armazenado.append(custoBenef[pos][2]) # 3n
            pesoMax -= custoBenef[pos][1] # 4n
            presente.add(pos) # n
            
    return armazenado, pesoMax 

# Função principal que executa a estratégia gulosa com temporização e exibição dos resultados
def estrategia_gulosa(pesoMax, custo, beneficio, tam, mochila):
    
    # Inicialização da variavel de tempo
    inicio = time.time()

    # Convertendo listas para arrays
    custo = np.array(custo)
    beneficio = np.array(beneficio)

    # Calcula o custo benefício de cada item
    custoBenef = calcular_custo_beneficio(custo, beneficio, tam)

    # Seleciona os itens para colocar na mochila
    armazenado, pesoMax = selecionar_itens(custoBenef, pesoMax, tam)

    # Finaliza o tempo da execução
    final = time.time() - inicio

    # Soma o benefício dos itens armazenados
    benefGulosa = 0
    for item in armazenado:
        benefGulosa += beneficio[item]  

    main.clear_terminal()

    # Printando os resultados com Rich
    Console().rule("Estratégia gulosa (Ordenado) com numba")
    table = Table(title=f"\nArquivo de entrada {mochila.entrada}", show_header=True, header_style="bold magenta")
    table.add_column("Custo benefício", justify="center", style="yellow", no_wrap=True)
    table.add_column("Peso máximo restante", justify="center", style="red", no_wrap=True)
    table.add_column("Tempo da estratégia gulosa", justify="center", style="purple", no_wrap=True)
    table.add_row(str(benefGulosa), str(pesoMax), str(final))

    console = Console()
    console.print(table, justify="center")
    Console().rule("")

    # Printa os itens armazenados
    Console().rule("")
    console.print(f"Os itens armazenados são: {armazenado}", style="bold green", justify="center")
    Console().rule("")

    return final, benefGulosa

# -------------------------------------------------------------------------------------------------------------------- #

# Função para ordenar os beneficios
def ordenar_beneficio(custoBenef):
    return sorted(custoBenef, key=lambda x: x[0])


# Função principal que executa a estratégia gulosa com temporização e exibição dos resultados
def estrategia_gulosa_com_ordenacao(pesoMax, custo, beneficio, tam, mochila):
    
    # Inicialização da variavel de tempo
    inicio = time.time()

    # Convertendo listas para arrays
    custo = np.array(custo)
    beneficio = np.array(beneficio)

    # Calcula o custo benefício de cada item
    custoBenef = calcular_custo_beneficio(custo, beneficio, tam)

    # Ordena os itens dentro da mochila
    custoBenef = ordenar_beneficio(custoBenef)

    # Seleciona os itens para colocar na mochila
    armazenado, pesoMax = selecionar_itens(custoBenef, pesoMax, tam)
    
    # Finaliza o tempo da execução
    final = time.time() - inicio

    # Soma o benefício dos itens armazenados
    benefGulosa = 0
    for item in armazenado:
        benefGulosa += beneficio[item]  

    main.clear_terminal()

    # Printando os resultados com Rich
    Console().rule("Estratégia gulosa com numba")
    table = Table(title=f"\nArquivo de entrada {mochila.entrada}", show_header=True, header_style="bold magenta")
    table.add_column("Custo benefício", justify="center", style="yellow", no_wrap=True)
    table.add_column("Peso máximo restante", justify="center", style="red", no_wrap=True)
    table.add_column("Tempo da estratégia gulosa", justify="center", style="purple", no_wrap=True)
    table.add_row(str(benefGulosa), str(pesoMax), str(final))

    console = Console()
    console.print(table, justify="center")
    Console().rule("")

    # Printa os itens armazenados
    Console().rule("")
    console.print(f"Os itens armazenados são: {armazenado}", style="bold green", justify="center")
    Console().rule("")

    return final, benefGulosa
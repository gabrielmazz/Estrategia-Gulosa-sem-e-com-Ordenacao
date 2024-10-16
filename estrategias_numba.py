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
    
    for i in range(tam):
        
        if custo[i] == 0:
            custoBenef.append((beneficio[i]/(custo[i]+1), custo[i], i))
        else:
            custoBenef.append((beneficio[i]/custo[i], custo[i], i))
            
    return custoBenef

# Função que seleciona os itens para colocar na mochila com base no custo benefício
# feito anteriormente pela outra função
@jit(nopython=True)
def selecionar_itens(custoBenef, pesoMax, tam):
    
    armazenado = []
    presente = set()
    
    # Percorre todos os itens que entrarament
    for i in range(tam):
        
        # Inicializa a variável de maior custo benefício
        maior = -999999
        
        for j in range(tam):
            if custoBenef[j][0] > maior and j not in presente:
                maior = custoBenef[j][0]
                pos = j
                
        if custoBenef[pos][1] <= pesoMax:
            armazenado.append(custoBenef[pos][2])
            pesoMax -= custoBenef[pos][1]
            presente.add(pos)
            
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

# -------------------------------------------------------------------------------------------------------------------- #

@jit(nopython=True)
def calculo_estrategia_programacao_dinamica(pesoMax, custo, beneficio, tam):
    
    # Inicializando a matriz de zeros usando NumPy
    matriz = np.zeros((tam + 1, pesoMax + 1), dtype=np.int32)
    maior = np.array([0, 0, 0], dtype=np.int32)

    # Preenche a matriz com os valores
    for i in range(1, tam + 1):  
        for j in range(pesoMax + 1):
            if custo[i - 1] > j:
                matriz[i][j] = matriz[i - 1][j]
            else:
                matriz[i][j] = max(matriz[i - 1][j], matriz[i - 1][j - custo[i - 1]] + beneficio[i - 1])
            if matriz[i][j] > maior[0]:
                maior[0] = matriz[i][j]
                maior[1] = i
                maior[2] = j

    # Recupera os itens armazenados
    itens = []
    for i in range(maior[1], 0, -1):
        
        if matriz[i][maior[2]] != matriz[i - 1][maior[2]]:
            itens.append(i - 1)
            maior[2] -= custo[i - 1]
            
            # Teste para verificar se o item foi armazenado
            pesoMaxRestante = maior[1] - i 

    return matriz, maior, itens, pesoMaxRestante


# Função principal que executa a estratégia de programação dinâmica com temporização e exibição dos resultados
def estrategia_programacao_dinamica(pesoMax, custo, beneficio, tam, mochila):
    
    # Inicializando a variavel de tempo
    inicio = time.time()

    # Chama a função otimizada com Numba
    matriz, maior, itens, pesoMaxRestante = calculo_estrategia_programacao_dinamica(pesoMax, custo, beneficio, tam)

    final = time.time() - inicio

    main.clear_terminal()

    # Printando os resultados
    Console().rule("Programação dinâmica com Numba")
    
    # Configuração da tabela
    table = Table(title=f"\nArquivo de entrada {mochila.entrada}", show_header=True, header_style="bold magenta")
    table.add_column("Custo benefício", justify="center", style="yellow", no_wrap=True)
    table.add_column("Peso máximo restante", justify="center", style="red", no_wrap=True)
    table.add_column("Tempo da programação dinâmica", justify="center", style="purple", no_wrap=True)
    table.add_row(str(maior[0]), str(pesoMaxRestante), str(final))
    
    # Criação do console e centralização da tabela
    console = Console()
    console.print(table, justify="center")
    Console().rule("")
    
    # Printa os itens armazenados
    Console().rule("")
    console.print(f"Os itens armazenados são: {itens}", style="bold green", justify="center")
    Console().rule("")

    return final, matriz[tam][pesoMax]

# -------------------------------------------------------------------------------------------------------------------- #

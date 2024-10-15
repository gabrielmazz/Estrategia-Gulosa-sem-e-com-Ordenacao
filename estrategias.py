import time
import numpy as np
from rich.console import Console
from rich.table import Table
from numba import jit

def estrategia_gulosa(pesoMax, custo, beneficio, tam, mochila):
    
    # Inicialização de variáveis
    armazenado = []
    custoBenef = []

    inicio = time.time()
    
    for i in range(tam): # Calcula o custo benefício de cada item # 2n + 2
        
        if custo[i] == 0: # Se o custo do item for zero # 2n
            custoBenef.append((beneficio[i]/(custo[i]+1), custo[i], i)) # Evita divisão por zero # 6n
        else:
            custoBenef.append((beneficio[i]/custo[i], custo[i], i)) # Calcula o custo benefício # 5n

    presente = set() # 1
    
    for i in range(tam): # 2n + 2 
        
        maior = -999999 # n
        
        for j in range(tam): # n (2n + 2) = 2n^2 + 2n
            if custoBenef[j][0] > maior and j not in presente: # 10n^2 + 10n
                maior = custoBenef[j][0] # 6n^2 + 6n
                pos = j # 2n^2 + 2n
                
        if custoBenef[pos][1] <= pesoMax: # Verifica se o peso do item é menor que o peso máximo # 3n
            armazenado.append(custoBenef[pos][2]) # Armazena o item # 3n
            pesoMax -= custoBenef[pos][1] # Subtrai o peso do item do peso máximo # 4n
            presente.add(pos) # Adiciona o item na lista de itens armazenados # n
            
    final = time.time() - inicio
    
    # 20n^2 + 44n + 5 pior caso
    # O(n^2)
    
    benefGulosa = 0

    # print("Armazenado: ", armazenado)
    for item in armazenado:
        benefGulosa += beneficio[item] # Soma o benefício dos itens armazenados

    # Printando os resultados
    Console().rule("Estratégia gulosa")
    
    # Configuração da tabela
    table = Table(title=f"\nArquivo de entrada {mochila.entrada}", show_header=True, header_style="bold magenta")
    table.add_column("Custo benefício", justify="center", style="cyan", no_wrap=True)
    table.add_column("Peso máximo restante", justify="center", style="cyan", no_wrap=True)
    table.add_column("Tempo da estratégia gulosa", justify="center", style="cyan", no_wrap=True)
    table.add_row(str(benefGulosa), str(pesoMax), str(final))

    # Criação do console e centralização da tabela
    console = Console()
    console.print(table, justify="center")
    Console().rule("")
    
    # Printa os itens armazenados
    Console().rule("")
    console.print(f"Os itens armazenados são: {armazenado}", style="bold green", justify="center")
    Console().rule("")
    
    return final, benefGulosa

def estrategia_programacao_dinamica(pesoMax, custo, beneficio, tam, mochila):
    
    matriz = []
    maior = [0, 0, 0]

    inicio = time.time()
    for i in range(tam+1): # Cria a matriz # 2 (n+1) + 2 = 2n + 4
        matriz.append([]) # n+1
        for j in range(pesoMax+1): # Preenche a matriz com zeros # (n+1) * (2 (m+1) + 2) = n+1 * (2m + 4) = 2mn + 4n + 2m + 4
            matriz[i].append(0) # 2 (m+1)(n+1) = 2mn + 2m + 2n + 2
    
    for i in range(1, tam+1): # Preenche a matriz # 2n + 2
        for j in range(pesoMax+1): # n (2m + 4) = 2mn + 4n
            if custo[i-1] > j: # Se o custo do item for maior que o peso máximo # 3 (m+1) n = 3mn + 3n
                matriz[i][j] = matriz[i-1][j] # A matriz recebe o valor da linha anterior # 6mn + 6n
            else: # Se não
                matriz[i][j] = max(matriz[i-1][j], matriz[i-1][j-custo[i-1]] + beneficio[i-1]) # A matriz recebe o maior valor entre o valor da linha anterior e o valor da linha anterior subtraído do custo do item e somado ao benefício do item # 16mn + 16n
            if matriz[i][j] > maior[0]: # Se o valor da matriz for maior que o valor armazenado # 4 (m+1) n = 4mn + 4n
                maior[0] = matriz[i][j] # O valor armazenado recebe o valor da matriz # 4mn + 4n
                maior[1] = i # A linha do valor armazenado recebe o valor de i # 3mn + 3n
                maior[2] = j # E a coluna do valor armazenado recebe o valor de j # 3mn + 3n

    itens = [] # 1
    for i in range(maior[1], 0, -1): # Percorre a matriz de trás para frente # 2n + 2
        if matriz[i][maior[2]] != matriz[i-1][maior[2]]: # Se o valor da matriz for diferente do valor da linha anterior # 8n
            itens.append(i-1) # Adiciona o item na lista de itens # 2n
            maior[2] -= custo[i-1] # Subtrai o custo do item do valor da coluna # 5n
            pesoMaxRestante = maior[1] - i # Teste para verificar se o item foi armazenado # 3n
    
    final = time.time() - inicio
    
    # Printando os resultados
    Console().rule("Programação dinâmica")
    
    # Configuração da tabela
    table = Table(title="Programação dinâmica", show_header=True, header_style="bold magenta")
    table.add_column("Custo benefício", justify="center", style="cyan", no_wrap=True)
    table.add_column("Peso máximo restante", justify="center", style="cyan", no_wrap=True)
    table.add_column("Tempo da programação dinâmica", justify="center", style="cyan", no_wrap=True)
    table.add_row(str(maior[0]), str(pesoMaxRestante), str(final))
    
    # Criação do console e centralização da tabela
    console = Console()
    console.print(table, justify="center")
    Console().rule("")
    
    # Printa os itens armazenados
    Console().rule("")
    console.print(f"Os itens armazenados são: {itens}", style="bold green", justify="center")
    Console().rule("")
    
    return final, matriz[len(custo)][pesoMax-1]
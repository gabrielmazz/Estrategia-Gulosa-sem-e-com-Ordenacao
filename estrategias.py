import time
from rich.console import Console
from rich.table import Table
from numba import jit
import main

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

    main.clear_terminal()

    # Printando os resultados
    Console().rule("Estratégia gulosa")
    
    # Configuração da tabela
    table = Table(title=f"\nArquivo de entrada {mochila.entrada}", show_header=True, header_style="bold magenta")
    table.add_column("Custo benefício", justify="center", style="yellow", no_wrap=True)
    table.add_column("Peso máximo restante", justify="center", style="red", no_wrap=True)
    table.add_column("Tempo da estratégia gulosa", justify="center", style="purple", no_wrap=True)
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

# -------------------------------------------------------------------------------------------------------------------- #


def estrategia_gulosa_com_ordenacao(pesoMax, custo, beneficio, tam, mochila):
    
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
    
    custoBenef.sort(reverse=True, key=lambda x: x[0])
    
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

    main.clear_terminal()

    # Printando os resultados
    Console().rule("Estratégia gulosa com ordenação")
    
    # Configuração da tabela
    table = Table(title=f"\nArquivo de entrada {mochila.entrada}", show_header=True, header_style="bold magenta")
    table.add_column("Custo benefício", justify="center", style="yellow", no_wrap=True)
    table.add_column("Peso máximo restante", justify="center", style="red", no_wrap=True)
    table.add_column("Tempo da estratégia gulosa", justify="center", style="purple", no_wrap=True)
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
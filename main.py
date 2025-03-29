from mochila import struct
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import estrategias
import estrategias_numba
import os

# Função para apagar o terminal
def clear_terminal():
    console = Console()
    console.clear()

if __name__ == '__main__':
    
    clear_terminal()
    
    # Determina qual o arquivo de entrada que será utilizado
    arquivo = Prompt.ask("Qual arquivo de entrada deseja utilizar?\n1 - Mochila10\n2 - Mochila50\n3 - Mochila100\n4 - Mochila200\n5 - Mochila300\n6 - Mochila500\n7 - Mochila1000\n8 - Mochila1250\n9 - Mochila1500\n10 - Mochila2000\n11 - Mochila2500\n12 - Mochila3000\n13 - Mochila4000\n14 - Mochila5000\n15 - Mochila10000\n16 - Mochila20000\n17 - Mochila30000\n18 - Mochila50000\n19 - Mochila100000\n\n", choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"])
    
    # Dicionário de mapeamento para os arquivos
    arquivos_mochila = {
        "1": './Entradas/Mochila10.txt',
        "2": './Entradas/Mochila50.txt',
        "3": './Entradas/Mochila100.txt',
        "4": './Entradas/Mochila200.txt',
        "5": './Entradas/Mochila300.txt',
        "6": './Entradas/Mochila500.txt',
        "7": './Entradas/Mochila1000.txt',
        "8": './Entradas/Mochila1250.txt',
        "9": './Entradas/Mochila1500.txt',
        "10": './Entradas/Mochila2000.txt',
        "11": './Entradas/Mochila2500.txt',
        "12": './Entradas/Mochila3000.txt',
        "13": './Entradas/Mochila4000.txt',
        "14": './Entradas/Mochila5000.txt',
        "15": './Entradas/Mochila10000.txt',
        "16": './Entradas/Mochila20000.txt',
        "17": './Entradas/Mochila30000.txt',
        "18": './Entradas/Mochila50000.txt',
        "19": './Entradas/Mochila100000.txt',
    }

    caminho_arquivo_entrada = arquivos_mochila[arquivo]

    # Verifica se o arquivo existe
    if os.path.exists(caminho_arquivo_entrada):
        print(f"Arquivo selecionado: {caminho_arquivo_entrada}")
    else:
        print(f"Erro: O arquivo {caminho_arquivo_entrada} não foi encontrado.")
        
    # Limpa o terminal
    clear_terminal()
        
    # Criação da classe
    mochila = struct(caminho_arquivo_entrada)
    
    # Abertura do arquivo
    arquivo = mochila.abrir_arquivo()
    
    # Armazenamento do arquivo
    mochila.armazena_arquivo(arquivo)
    
    
    # Determina se será a estratégia gulosa ou programação dinâmica
    estrategia = Prompt.ask("Deseja utilizar a estratégia gulosa ou programação dinâmica?\n1 - Estrátegia Gulosa\n2 - Estrátegia Gulosa com Ordenação\n\n", choices=["1", "2"])
    
    clear_terminal()
    
    # Determina se o usuário utilizara a otimização pelo Numba ou pelo Python puro
    numba = Prompt.ask("Deseja utilizar o Numba para otimização?\n1 - Sim\n2 - Não\n\n", choices=["1", "2"])
    
    clear_terminal()
    
    # Salva os input na classe
    mochila.define_estrategia_otimizacao(estrategia, numba)
    
    match estrategia:
        case "1":
            if numba == "1":
                tempfinal, benefGulosa = estrategias_numba.estrategia_gulosa(mochila.pesoMax, mochila.custo, mochila.beneficio, len(mochila.beneficio), mochila)
            else:
                tempfinal, benefGulosa = estrategias.estrategia_gulosa(mochila.pesoMax, mochila.custo, mochila.beneficio, len(mochila.beneficio), mochila)
        case "2":
            if numba == "1":
                tempfinal, benefGulosa = estrategias_numba.estrategia_gulosa_com_ordenacao(mochila.pesoMax, mochila.custo, mochila.beneficio, len(mochila.beneficio), mochila)
            else:
                tempfinal, benefGulosa = estrategias.estrategia_gulosa_com_ordenacao(mochila.pesoMax, mochila.custo, mochila.beneficio, len(mochila.beneficio), mochila)
                
    
    # Salva valores
    mochila.salva_valores(tempfinal, benefGulosa)
    
    # Escreve arquivo txt
    mochila.escreve_arquivo_txt()

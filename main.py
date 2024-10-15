from mochila import struct
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import estrategias
import estrategias_numba

if __name__ == '__main__':
    
    # Determina qual o arquivo de entrada que será utilizado
    arquivo = Prompt.ask("Qual arquivo de entrada deseja utilizar?\n1 - Mochila10\n2 - Mochila50\n3 - Mochila100\n4 - Mochila200\n5 - Mochila300\n6 - Mochila500\n7 - Mochila1000\n8 - Mochila1250\n9 - Mochila1500\n10 - Mochila2000\n11 - Mochila2500\n12 - Mochila3000\n13 - Mochila4000\n14 - Mochila5000\n\n", choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"])
    
    match arquivo:
        case "1":
            caminho_arquivo_entrada = './Entradas/Mochila10.txt'
        case "2":
            caminho_arquivo_entrada = './Entradas/Mochila50.txt'
        case "3":
            caminho_arquivo_entrada = './Entradas/Mochila100.txt'
        case "4":
            caminho_arquivo_entrada = './Entradas/Mochila200.txt'
        case "5":
            caminho_arquivo_entrada = './Entradas/Mochila300.txt'
        case "6":
            caminho_arquivo_entrada = './Entradas/Mochila500.txt'
        case "7":
            caminho_arquivo_entrada = './Entradas/Mochila1000.txt'
        case "8":
            caminho_arquivo_entrada = './Entradas/Mochila1250.txt'
        case "9":
            caminho_arquivo_entrada = './Entradas/Mochila1500.txt'
        case "10":
            caminho_arquivo_entrada = './Entradas/Mochila2000.txt'
        case "11":
            caminho_arquivo_entrada = './Entradas/Mochila2500.txt'
        case "12":
            caminho_arquivo_entrada = './Entradas/Mochila3000.txt'
        case "13":
            caminho_arquivo_entrada = './Entradas/Mochila4000.txt'
        case "14":
            caminho_arquivo_entrada = './Entradas/Mochila5000.txt'
        
    # Criação da classe
    mochila = struct(caminho_arquivo_entrada)
    
    # Abertura do arquivo
    arquivo = mochila.abrir_arquivo()
    
    # Armazenamento do arquivo
    mochila.armazena_arquivo(arquivo)
    
    
    # Determina se será a estratégia gulosa ou programação dinâmica
    estrategia = Prompt.ask("Deseja utilizar a estratégia gulosa ou programação dinâmica?\n1 - Estrátegia Gulosa\n2 - Programação Dinâmica\n\n", choices=["1", "2"])
    
    # Determina se o usuário utilizara a otimização pelo Numba ou pelo Python puro
    numba = Prompt.ask("Deseja utilizar o Numba para otimização?\n1 - Sim\n2 - Não\n\n", choices=["1", "2"])
    
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
                tempfinal, benefGulosa = estrategias_numba.estrategia_programacao_dinamica(mochila.pesoMax, mochila.custo, mochila.beneficio, len(mochila.beneficio), mochila)
            else:
                tempfinal, benefGulosa = estrategias.estrategia_programacao_dinamica(mochila.pesoMax, mochila.custo, mochila.beneficio, len(mochila.beneficio), mochila)
                
    
    # Salva valores
    mochila.salva_valores(tempfinal, benefGulosa)
    
    # Escreve arquivo txt
    mochila.escreve_arquivo_txt()

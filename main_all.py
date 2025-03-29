from mochila import struct
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import estrategias
import estrategias_numba
import os
import time

# Função para apagar o terminal
def clear_terminal():
    console = Console()
    console.clear()

if __name__ == '__main__':
    
    # Limpa o terminal
    clear_terminal()
    
    # Dicionário de mapeamento para os arquivos
    arquivos_mochila = {
        "0": './Entradas/Mochila10.txt',
        "1": './Entradas/Mochila50.txt',
        "2": './Entradas/Mochila100.txt',
        "3": './Entradas/Mochila200.txt',
        "4": './Entradas/Mochila300.txt',
        "5": './Entradas/Mochila500.txt',
        "6": './Entradas/Mochila750.txt',
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
    
    # Determina a estratégia e a otimização apenas uma vez
    estrategia = Prompt.ask("Deseja utilizar a estratégia gulosa ou estratégia gulosa com ordenação ?\n1 - Estratégia Gulosa\n2 - Estratégia Gulosa com Ordenação\n\n", choices=["1", "2"])
    clear_terminal()
    numba = Prompt.ask("Deseja utilizar o Numba para otimização?\n1 - Sim\n2 - Não\n\n", choices=["1", "2"])
    clear_terminal()
    
    # Loop para cada arquivo
    tempos_execucao = []

    for key, caminho_arquivo_entrada in arquivos_mochila.items():
        
        # Verifica se o arquivo existe
        if os.path.exists(caminho_arquivo_entrada):
            print(f"Processando arquivo: {caminho_arquivo_entrada}")
        else:
            print(f"Erro: O arquivo {caminho_arquivo_entrada} não foi encontrado.")
            continue  # Pula para o próximo arquivo se o arquivo atual não for encontrado
        
        for i in range(1):
            
            # Limpa o terminal
            clear_terminal()

            # Inicia a contagem de tempo
            tempo_inicio = time.time()
            
            # Criação da classe com o arquivo de entrada
            mochila = struct(caminho_arquivo_entrada)
            
            # Abertura e armazenamento do arquivo
            arquivo = mochila.abrir_arquivo()
            
            mochila.armazena_arquivo(arquivo)
            
            # Define a estratégia e otimização uma vez
            mochila.define_estrategia_otimizacao(estrategia, numba)
            
            # Escolha da estratégia baseada na seleção do usuário e se usa Numba ou não
            match estrategia:
                case "1":
                    if numba == "1":
                        tempfinal, benefGulosa = estrategias_numba.estrategia_gulosa(
                            mochila.pesoMax, mochila.custo, mochila.beneficio, len(mochila.beneficio), mochila
                        )
                        tipo_estrategia = "Gulosa com Numba"
                    else:
                        tempfinal, benefGulosa = estrategias.estrategia_gulosa(
                            mochila.pesoMax, mochila.custo, mochila.beneficio, len(mochila.beneficio), mochila
                        )
                        tipo_estrategia = "Gulosa sem Numba"
                case "2":
                    if numba == "1":
                        tempfinal, benefGulosa = estrategias_numba.estrategia_gulosa_com_ordenacao(
                            mochila.pesoMax, mochila.custo, mochila.beneficio, len(mochila.beneficio), mochila
                        )
                        tipo_estrategia = "Gulosa com Ordenação e Numba"
                    else:
                        tempfinal, benefGulosa = estrategias.estrategia_gulosa_com_ordenacao(
                            mochila.pesoMax, mochila.custo, mochila.beneficio, len(mochila.beneficio), mochila
                        )
                        tipo_estrategia = "Gulosa com Ordenação sem Numba"
            
            # Finaliza a contagem de tempo e armazena o tempo de execução
            tempo_fim = time.time()
            tempo_execucao = tempo_fim - tempo_inicio
            
            
            
            # Salva os resultados na classe
            # mochila.salva_valores(tempfinal, benefGulosa)
            
            # Escreve o arquivo txt com os resultados para o arquivo atual
            # mochila.escreve_arquivo_txt()
            
            # Limpa o terminal após processar cada arquivo
            #clear_terminal()
        

        # Calcula a média dos tempos de execução
        #media_tempo_execucao = sum(tempos_execucao) / len(tempos_execucao)
        
        # Escreve qual mochila foi utilizada pegando apenas o numero do caminho
        numero_mochila = caminho_arquivo_entrada.split("/")[-1].split(".")[0]
        
        # Retira o "Mochila" do nome do arquivo
        numero_mochila = numero_mochila.replace("Mochila", "")
         
        # Escre os resultados em um arquivo
        with open(f'./Resultados/Resultado_{numero_mochila}_{tipo_estrategia}.txt', 'w') as arquivo:
            
            if estrategia == "1":
                if numba == "1":
                    
                    if os.path.exists(f'./Resultados/Resultado_{numero_mochila}_Gulosa_Numba.txt'):
                        os.remove(f'./Resultados/Resultado_{numero_mochila}_Gulosa_Numba.txt')
                    
                    arquivo.write("Estratégia Gulosa com otimização Numba\n")
                    
                else:
                    
                    if os.path.exists(f'./Resultados/Resultado_{numero_mochila}_Gulosa.txt'):
                        os.remove(f'./Resultados/Resultado_{numero_mochila}_Gulosa.txt')
                    
                    arquivo.write("Estratégia Gulosa sem otimização Numba\n")
            else:
                if numba == "1":
                    
                    if os.path.exists(f'./Resultados/Resultado_{numero_mochila}_Gulosa_Ordenado_Numba.txt'):
                        os.remove(f'./Resultados/Resultado_{numero_mochila}_Gulosa_Ordenado_Numba.txt')
                    
                    arquivo.write("Estratégia Gulosa com Ordenação e otimização Numba\n")
                else:
                    
                    if os.path.exists(f'./Resultados/Resultado_{numero_mochila}_Gulosa_Ordenado.txt'):
                        os.remove(f'./Resultados/Resultado_{numero_mochila}_Gulosa_Ordenado.txt')
                        
                    arquivo.write("Estratégia Gulosa com Ordenação sem otimização Numba\n")
            
            arquivo.write(f"Arquivo de entrada: {caminho_arquivo_entrada}\n")
            arquivo.write(f"Tempo médio de execução: {tempo_execucao:.10f} segundos\n")
            arquivo.write(f"Benefício total: {benefGulosa}\n")
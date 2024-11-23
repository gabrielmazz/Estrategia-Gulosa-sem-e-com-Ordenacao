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
    
    
    lista_tempo_guloso_sem_ordenacao = []
    lista_tempo_guloso_com_ordenacao = []
    lista_tempo_guloso_sem_ordenacao_numba = []
    lista_tempo_guloso_com_ordenacao_numba = []
        
    
    # Loop para cada arquivo
    tempos_execucao = []

    for key, caminho_arquivo_entrada in arquivos_mochila.items():
        
        # Verifica se o arquivo existe
        if os.path.exists(caminho_arquivo_entrada):
            print(f"Processando arquivo: {caminho_arquivo_entrada}")
        else:
            print(f"Erro: O arquivo {caminho_arquivo_entrada} não foi encontrado.")
            continue  # Pula para o próximo arquivo se o arquivo atual não for encontrado
        
        # Executa o processo 6 vezes para cálculo da média de tempo
        for i in range(6):
            
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
            tempos_execucao.append(tempo_execucao)
            
            
            # Salva os resultados na classe
            # mochila.salva_valores(tempfinal, benefGulosa)
            
            # Escreve o arquivo txt com os resultados para o arquivo atual
            # mochila.escreve_arquivo_txt()
            
            # Limpa o terminal após processar cada arquivo
            #clear_terminal()
        

        # Calcula a média dos tempos de execução
        media_tempo_execucao = sum(tempos_execucao) / len(tempos_execucao)
        
        if tipo_estrategia == "Gulosa sem Numba":
            lista_tempo_guloso_sem_ordenacao.append(media_tempo_execucao)
        elif tipo_estrategia == "Gulosa com Ordenação sem Numba":
            lista_tempo_guloso_com_ordenacao.append(media_tempo_execucao)
        elif tipo_estrategia == "Gulosa com Numba":
            lista_tempo_guloso_sem_ordenacao_numba.append(media_tempo_execucao)
        elif tipo_estrategia == "Gulosa com Ordenação e Numba":
            lista_tempo_guloso_com_ordenacao_numba.append(media_tempo_execucao)
            
        print(lista_tempo_guloso_sem_ordenacao)
        
        # Escreve a média de tempo no arquivo de resultados com informações adicionais
        with open(f"resultados_{key}.txt", "a") as arquivo_resultado:
            arquivo_resultado.write(f"\nEstratégia utilizada: {tipo_estrategia}\n")
            arquivo_resultado.write(f"Média de tempo de execução para {caminho_arquivo_entrada}: {media_tempo_execucao:.4f} segundos\n")
                
        # Limpa a lista de tempos para o próximo arquivo
        tempos_execucao.clear()

    print("Processamento concluído para todos os arquivos.") 
    
    # Escreve as listas de tempo em um arquivo de resultados
    with open("resultados.txt", "a") as arquivo_resultado: 
        
        if lista_tempo_guloso_sem_ordenacao:
            media_tempo_guloso_sem_ordenacao = sum(lista_tempo_guloso_sem_ordenacao) / len(lista_tempo_guloso_sem_ordenacao)
            arquivo_resultado.write(f"Média de tempo de execução para Estratégia Gulosa sem Numba: {media_tempo_guloso_sem_ordenacao:.4f} segundos\n")
            arquivo_resultado.write(f"Lista de tempos: {lista_tempo_guloso_sem_ordenacao}\n")
            arquivo_resultado.write("\n")
            
        if lista_tempo_guloso_com_ordenacao:
            media_tempo_guloso_com_ordenacao = sum(lista_tempo_guloso_com_ordenacao) / len(lista_tempo_guloso_com_ordenacao)
            arquivo_resultado.write(f"Média de tempo de execução para Estratégia Gulosa com Ordenação sem Numba: {media_tempo_guloso_com_ordenacao:.4f} segundos\n")
            arquivo_resultado.write(f"Lista de tempos: {lista_tempo_guloso_com_ordenacao}\n")
            arquivo_resultado.write("\n")
            
        if lista_tempo_guloso_sem_ordenacao_numba:
            media_tempo_guloso_sem_ordenacao_numba = sum(lista_tempo_guloso_sem_ordenacao_numba) / len(lista_tempo_guloso_sem_ordenacao_numba)
            arquivo_resultado.write(f"Média de tempo de execução para Estratégia Gulosa com Numba: {media_tempo_guloso_sem_ordenacao_numba:.4f} segundos\n")
            arquivo_resultado.write(f"Lista de tempos: {lista_tempo_guloso_sem_ordenacao_numba}\n")
            arquivo_resultado.write("\n")
            
        if lista_tempo_guloso_com_ordenacao_numba:
            media_tempo_guloso_com_ordenacao_numba = sum(lista_tempo_guloso_com_ordenacao_numba) / len(lista_tempo_guloso_com_ordenacao_numba)
            arquivo_resultado.write(f"Média de tempo de execução para Estratégia Gulosa com Ordenação e Numba: {media_tempo_guloso_com_ordenacao_numba:.4f} segundos\n")
            arquivo_resultado.write(f"Lista de tempos: {lista_tempo_guloso_com_ordenacao_numba}\n")
            arquivo_resultado.write("\n")
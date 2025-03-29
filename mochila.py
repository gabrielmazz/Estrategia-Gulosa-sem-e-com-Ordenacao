import time
import os

class struct:
    
    def __init__(self, caminho):
        
        self.caminho_arquivo_entrada = caminho
        
        self.lista_tempo_guloso_sem_ordenacao = []
        self.lista_tempo_guloso_com_ordenacao = []
        self.lista_tempo_guloso_sem_ordenacao_numba = []
        self.lista_tempo_guloso_com_ordenacao_numba = []
        
    def separa_entrada(self):
        # Está função pega o valor que está no caminho de entrada, por exemplo:
        # ./Entradas/Mochila10.txt -> pegando o valor 10
        self.entrada = int(self.caminho_arquivo_entrada.split('Mochila')[1].split('.')[0])
        
    def abrir_arquivo(self):
        try:
            arquivo = open(self.caminho_arquivo_entrada, 'r')
            self.separa_entrada() 
            return arquivo
        except FileNotFoundError:
            print('Arquivo não encontrado')
            return None
     
   
        
    def armazena_arquivo(self, arquivo):
        
        self.beneficio = []
        self.custo = []
        self.pesoMax = arquivo.readline()
        self.pesoMax = int(self.pesoMax)
    
        inicio = time.time()
    
        bl = arquivo.readline()
        bls = bl.split()
        for item in bls:
            self.beneficio.append(int(item))
    
        cl = arquivo.readline()
        cls = cl.split()
        for item in cls:
            self.custo.append(int(item))
        
        self.tempo_abertura_arquivo = time.time() - inicio
        
    def define_estrategia_otimizacao(self, estrategia, otimizacao):
        self.estrategia = estrategia
        self.otimizacao = otimizacao
        
    def salva_valores(self, tempfinal, benefGulosa):
        self.tempo_final = tempfinal
        self.benefGulosa = benefGulosa
        
    def escreve_arquivo_txt(self):
        
        with open(f'./Resultados/Resultado_{self.entrada}.txt', 'w') as arquivo:
            
            # Verifica qual estratégia foi utilizada e se teve otimização
            if self.estrategia == "1":
                if self.otimizacao == "1":
                    
                    # Verifica se o arquivo existe na pasta
                    if os.path.exists(f'./Resultados/Resultado_{self.entrada}_Gulosa_Numba.txt'):
                        os.remove(f'./Resultados/Resultado_{self.entrada}_Gulosa_Numba.txt')    
                    
                    arquivo.write("Estratégia Gulosa com otimização Numba\n")
                    os.rename(f'./Resultados/Resultado_{self.entrada}.txt', f'./Resultados/Resultado_{self.entrada}_Gulosa_Numba.txt')
                    
                else:
                    # Verifica se o arquivo existe na pasta
                    if os.path.exists(f'./Resultados/Resultado_{self.entrada}_Gulosa.txt'):
                        os.remove(f'./Resultados/Resultado_{self.entrada}_Gulosa.txt')    
                    
                    arquivo.write("Estratégia Gulosa sem otimização Numba\n")
                    os.rename(f'./Resultados/Resultado_{self.entrada}.txt', f'./Resultados/Resultado_{self.entrada}_Gulosa.txt')
                    
            else:
                if self.otimizacao == "1":
                    
                    # Verifica se o arquivo existe na pasta
                    if os.path.exists(f'./Resultados/Resultado_{self.entrada}_Gulosa_Ordenacao_Numba.txt'):
                        os.remove(f'./Resultados/Resultado_{self.entrada}_Gulosa_Ordenacao_Numba.txt')    
                    
                    arquivo.write("Estratégia Gulosa com ordenação e otimização Numba\n")
                    os.rename(f'./Resultados/Resultado_{self.entrada}.txt', f'./Resultados/Resultado_{self.entrada}_Gulosa_Ordenacao_Numba.txt')
                    
                else:
                    
                    # Verifica se o arquivo existe na pasta
                    if os.path.exists(f'./Resultados/Resultado_{self.entrada}_Gulosa_Ordenacao.txt'):
                        os.remove(f'./Resultados/Resultado_{self.entrada}_Gulosa_Ordenacao.txt')    
                    
                    arquivo.write("Estratégia Gulosa com ordenação sem otimização Numba\n")
                    os.rename(f'./Resultados/Resultado_{self.entrada}.txt', f'./Resultados/Resultado_{self.entrada}_Gulosa_Ordenacao.txt')
            
            arquivo.write(f"Arquivo de entrada: {self.caminho_arquivo_entrada}\n")
            arquivo.write(f"Tempo de abertura do arquivo: {self.tempo_abertura_arquivo:.10f}\n")
            
            if self.otimizacao == "1":
                arquivo.write(f"Tempo da estratégia gulosa: {self.tempo_final:.10f}\n")
                arquivo.write(f"Benefício total da estratégia gulosa: {self.benefGulosa}\n")
                
            else:
                arquivo.write(f"Tempo da estratégia gulosa com ordenação: {self.tempo_final:.10f}\n")
                arquivo.write(f"Benefício total da estratégia gulosa com ordenação: {self.benefGulosa}\n")
                
        arquivo.close()
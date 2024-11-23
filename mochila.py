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
        
        with open(f'Resultado_{self.entrada}.txt', 'w') as arquivo:
            
            # Verifica qual estratégia foi utilizada e se teve otimização
            if self.estrategia == "1":
                if self.otimizacao == "1":
                    
                    # Verifica se o arquivo existe na pasta
                    if os.path.exists(f'Resultado_{self.entrada}_Gulosa_Numba.txt'):
                        os.remove(f'Resultado_{self.entrada}_Gulosa_Numba.txt')    
                    
                    arquivo.write("Estratégia gulosa com otimização Numba\n")
                    os.rename(f'Resultado_{self.entrada}.txt', f'Resultado_{self.entrada}_Gulosa_Numba.txt')
                   
                else:
                    
                    if os.path.exists(f'Resultado_{self.entrada}_Gulosa.txt'):
                        os.remove(f'Resultado_{self.entrada}_Gulosa.txt')
                
                    arquivo.write("Estratégia gulosa sem otimização\n")
                    os.rename(f'Resultado_{self.entrada}.txt', f'Resultado_{self.entrada}_Gulosa.txt')
            else:
                
                if self.otimizacao == "1":
                
                    # Verifica se o arquivo existe na pasta
                    if os.path.exists(f'Resultado_{self.entrada}_Gulosa_Numba_Ordenada.txt'):
                        os.remove(f'Resultado_{self.entrada}_Gulosa_Numba_ordenada.txt')    
                   
                    arquivo.write("Estratégia gulosa (Ordenada) com otimização Numba\n")
                    os.rename(f'Resultado_{self.entrada}.txt', f'Resultado_{self.entrada}_Gulosa_Numba_Ordenada.txt')

                else:
                    
                    if os.path.exists(f'Resultado_{self.entrada}_Gulosa_Ordenada.txt'):
                        os.remove(f'Resultado_{self.entrada}_Gulosa_Ordenada.txt')
                    
                    arquivo.write("Estratégia gulosa (Ordenada) sem otimização\n")
                    os.rename(f'Resultado_{self.entrada}.txt', f'Resultado_{self.entrada}_Gulosa_Ordenada.txt')
        
            arquivo.write(f"Arquivo de entrada: {self.entrada}\n")
            arquivo.write(f"Tempo de abertura do arquivo: {self.tempo_abertura_arquivo:.10f}\n")
            
            if self.estrategia == "1":
                arquivo.write(f"Tempo da estratégia gulosa: {self.tempo_final:.10f}\n")
                arquivo.write(f"Benefício da estratégia gulosa: {self.benefGulosa}\n")
            else:
                arquivo.write(f"Tempo da estratégia gulosa (Ordenada): {self.tempo_final:.10f}\n")
                arquivo.write(f"Benefício da estratégia gulosa (Ordenada): {max(self.beneficio)}\n")
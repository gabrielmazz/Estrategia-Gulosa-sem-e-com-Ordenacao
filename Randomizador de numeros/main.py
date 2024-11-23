import random

# Path to the file
file_path = 'random_numbers.txt'

# Gerador de numeros aleatorios para teste, algo semelhante com:

# Randomizador de números

# Função para gerar números aleatórios para o benefício e custo
def random_numbers():

    # Loop para gerar 10000 números aleatórios
    for i in range(1000000):
        number = random.randint(1, 50)
        
        # Escreve o número no arquivo indicado no path
        file.write(f"{number} ")
            
def random_numbers_peso():

        number = random.randint(800000, 1000000)
        
        file.write(f"{number}\n")
        
if __name__ == '__main__':
    
    with open(file_path, 'a') as file:
        random_numbers_peso()
        
        random_numbers()
        
        file.write("\n")
        
        random_numbers()
        
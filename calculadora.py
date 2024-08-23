# Função para exibir o menu e obter a escolha do usuário
def menu():
    print("Selecione a operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

# Função para realizar a operação de adição
def adicionar(x, y):
    return x + y

# Função para realizar a operação de subtração
def subtrair(x, y):
    return x - y

# Função para realizar a operação de multiplicação
def multiplicar(x, y):
    return x * y

# Função para realizar a operação de divisão
def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    else:
        return x / y

# Função principal da calculadora
def calculadora():
    menu()
    
    # Obter a escolha do usuário
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")
    
    # Verificar se a escolha é válida
    if escolha in ('1', '2', '3', '4'):
        # Obter os números para a operação
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Executar a operação com base na escolha
        if escolha == '1':
            print(f"Resultad

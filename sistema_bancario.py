import datetime

def menu():
    """
    Exibe o menu exibindo as opções na tela para o usuário.
    """
     
    menu = """

    ========== MENU ==========

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastro
    [q] Sair

    ==========================

    => """

    return input(menu)

def depositar(saldo, extrato, /): #Somente argumentos sequenciais para o exercício
    """
    Realiza um depósito na conta do usuário.

    Parâmetros:
    saldo (float): O saldo atual da conta.
    extrato (str): O extrato atual da conta.

    Retorna:
    tuple: Um tuple contendo o novo saldo e o extrato atualizado.
    """

    while True: #Loop aninhado até que o usuário insira um valor válido e positivo
        try:
            deposito = float(input("\nPor favor, insira o valor do depósito:\nR$ "))
            if deposito > 0:
                break
            else:
                print("Por favor, insira um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.") #tratamento de exceção "ValueError"

    saldo += deposito #Adiciona valor inserido pelo usuário ao saldo total
    extrato += f"Depósito de R$ {deposito:.2f}\n" #Registra o depósito no extrato
    print(f"Depósito de R$ {deposito:.2f} efetuado com sucesso! Saldo atual: R$ {saldo:.2f}") #Informa ao usuário o sucesso da operação

    return saldo, extrato

def sacar(*, limite, limite_saques_diarios, saldo, extrato, saques_diarios, data_ultimo_saque): #Somente argumentos nomeados para o exercício
    """
    Realiza um saque na conta do usuário.

    Parâmetros:
    limite (float): O limite do valor do saque.
    limite_saques_diarios (int): O limite de saques diários em uma mesma conta.
    saldo (float): O saldo atual da conta.
    extrato (str): O extrato atual da conta.
    saques_diarios (int): O número de saques realizados na conta no dia atual.
    data_ultimo_saque (date): A data do último saque.

    Retorna:
    tuple: Um tuple contendo o novo saldo, extrato, número de saques diários e a data do último saque atualizada.
    """

    while True: #Loop aninhado até que seja inserido um valor de saque válido
            hoje = datetime.date.today() #Armazena a data atual

            saque = 0

            if data_ultimo_saque is None or data_ultimo_saque != hoje: #Verifica se os saque são de um novo dia
                saques_diarios = 0 #Reseta o contador de saques diários
                data_ultimo_saque = hoje

            if saques_diarios >= limite_saques_diarios:
                print("Você já atingiu o limite de 3 saques diários.")
                break

            try:
                saque = float(input("\nPor favor, insira o valor a ser sacado:\nR$ "))
                if saque < 0:
                    print("Por favor, insira um valor positivo")
                elif saque > limite:
                    print("O limite por saque é de R$ 500, por favor tente novamente.")
                elif saque > saldo:
                    print("Saldo insuficiente.")
                else:
                    saldo -= saque #Subtraí o valor sacado pelo usuário do saldo da conta
                    extrato += f"Saque de R$ {saque:.2f}\n" #Registra o saque no extrato
                    saques_diarios += 1 #Adiciona o saque ao contador se saques diários
                    print(f"Saque de R$ {saque:.2f} efetuado com sucesso! Saldo atual: R$ {saldo:.2f}") #Informa sucesso da operação e valor do saque e saldo em conta atual
                    print(f"Você ainda pode realizar {limite_saques_diarios - saques_diarios} saque(s) hoje.") #Informa o limite de saques diários
                    break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")

    return saldo, extrato, saques_diarios, data_ultimo_saque

def exibir_extrato(saldo, /, *, extrato): #Argumentos posicionais e nomeados para o exercício
    """
    Exibe o extrato na tela para o usuário.

    Parâmetros:
    saldo (float): O saldo atual da conta.
    extrato (str): O extrato atual da conta.

    Retorna:
    tuple: Um tuple contendo o saldo e o extrato atual.
    """

    print("\n======== EXTRATO ========\n")
    print("Sem movimentações." if not extrato else extrato) #Exibe extrato na tela
    print(f"\nSaldo: R$ {saldo:.2f}") #Exibe saldo na tela
    print("\n=========================")

    return saldo, extrato

def cadastrar_cliente(clientes):
    """
    Cadastra um novo cliente na lista de clientes.

    Parâmetros:
    clientes (list): Lista de clientes cadastrados no sistema.

    Retorna:
    dict: Um dicionario contendo o novo cliente para a lista de clientes cadastrados.
    """

    cpf = input("\nInforme o CPF do cliente (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nO CPF informado já está cadastrado!")
        return
    
    nome = input("Informe o nome completo do cliente: ")
    data_nascimento = input("Informe a data de nascimento no formato (dd/mm/aaaa): ")
    endereco = input("Informe o endereço no formato(logradouro, número - bairro - cidade/sigla estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nCliente cadastrado com sucesso!")

def filtrar_cliente(cpf, clientes):
    """
    Busca um CPF na lista de clientes cadastrados.

    Parâmetros:
    cpf (str): CPF do novo cliente a ser cadastrado.
    clientes (list): Lista de clientes cadastrados no sistema.

    Retorna:
    dict ou None: O dicionário do cliente se encontrado, caso contrário, retorna None.
    """

    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def main():
    """
    Inicia o loop do menu exibindo as opções na tela para o usuário.
    """
    
    LIMITE = 500
    LIMITE_SAQUES_DIARIOS = 3
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    saques_diarios = 0
    data_ultimo_saque = None
    clientes = []
    contas = []

    while True: #Loop do menu
        opcao = menu()

        if opcao == "d": #Módulo de Depósito
            saldo, extrato = depositar(saldo, extrato) #Atualiza saldo e extrato com os valores retornados pela função

        elif opcao == "s": #Módulo de Saque
            saldo, extrato, saques_diarios, data_ultimo_saque = sacar(limite=LIMITE, limite_saques_diarios=LIMITE_SAQUES_DIARIOS, saldo=saldo, extrato=extrato, saques_diarios=saques_diarios, data_ultimo_saque=data_ultimo_saque)

        elif opcao == "e": #Módulo de Extrato
            saldo, extrato = exibir_extrato(saldo, extrato=extrato)

        elif opcao == "c": #Módulo de Cadastro de Clientes
            cadastrar_cliente(clientes)
            
        elif opcao == "q": #Encerra o serviço
            print("\nObrigada pela preferência, até mais!\n")
            break #Quebra o loop do menu

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.") #Retorna para o usuário erro caso selecione opção não existente no menu

main()

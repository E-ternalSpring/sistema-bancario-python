import datetime

# Constantes
LIMITE = 500
LIMITE_SAQUES_DIARIOS = 3

# Variáveis globais
saldo = 0
extrato = ""
saques_diarios = 0
data_ultimo_saque = None

menu = """

========== MENU ==========

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==========================

=> """

while True: #Loop do menu
    opcao = input(menu)

    if opcao == "d": #Módulo de Depósito
        deposito = 0

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

    elif opcao == "s": #Módulo de Saque
        saque = 0

        while True: #Loop aninhado até que seja inserido um valor de saque válido
            hoje = datetime.date.today() #Armazena a data atual

            if data_ultimo_saque is None or data_ultimo_saque != hoje: #Verifica se os saque são de um novo dia
                saques_diarios = 0 #Reseta o contador de saques diários
                data_ultimo_saque = hoje

            if saques_diarios >= LIMITE_SAQUES_DIARIOS:
                print("Você já atingiu o limite de 3 saques diários.")
                break

            try:
                saque = float(input("\nPor favor, insira o valor a ser sacado:\nR$ "))
                if saque < 0:
                    print("Por favor, insira um valor positivo")
                elif saque > LIMITE:
                    print("O limite por saque é de R$ 500, por favor tente novamente.")
                elif saque > saldo:
                    print("Saldo insuficiente.")
                else:
                    saldo -= saque #Subtraí o valor sacado pelo usuário do saldo da conta
                    extrato += f"Saque de R$ {saque:.2f}\n" #Registra o saque no extrato
                    saques_diarios += 1 #Adiciona o saque ao contador se saques diários
                    print(f"Saque de R$ {saque:.2f} efetuado com sucesso! Saldo atual: R$ {saldo:.2f}") #Informa sucesso da operação e valor do saque e saldo em conta atual
                    print(f"Você ainda pode realizar {LIMITE_SAQUES_DIARIOS - saques_diarios} saque(s) hoje.") #Informa o limite de saques diários
                    break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")

    elif opcao == "e": #Módulo de Extrato
        print("\n======== EXTRATO ========\n")
        print("Sem movimentações." if not extrato else extrato) #Exibe extrato na tela
        print(f"\nSaldo: R$ {saldo:.2f}") #Exibe saldo na tela
        print("\n=========================")

    elif opcao == "q": #Encerra o serviço
        print("\nObrigada pela preferência, até mais!\n")
        break #Quebra o loop do menu

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.") #Retorna para o usuário erro caso selecione opção não existente no menu

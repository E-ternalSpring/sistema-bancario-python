menu = """

========== MENU ==========

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==========================

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: #Loop do menu

    opcao = input(menu) #Registra a opção inserida pelo usuário

    if opcao == "d": #Opção "Depositar"

        deposito = 0

        while True: #Loop aninhado até que o usuário insira um valor válido, positivo e inteiro
            try:
                deposito = int(input("\nPor favor, insira o valor do depósito:\nR$ "))
                if deposito > 0:
                    break
                else:
                    print("Por favor, insira um valor positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.") #tratamento de exceção "ValueError"

        saldo += deposito #Adiciona valor inserido pelo usuário ao saldo total
        extrato += f"Depósito de R$ {deposito}\n" #Registra o depósito no extrato
        print(f"Depósito de R$ {deposito} efetuado com sucesso! Saldo atual: R$ {saldo}") #Informa ao usuário o sucesso da operação

    elif opcao == "s":
        print("\nSaque")

    elif opcao == "e":
        print(f"\nExtrato:\n{extrato}") #Exibe na tela do usuário o extrato da conta

    elif opcao == "q": #Encerra o serviço
        print("\nObrigada pela preferência, até mais!\n")
        break #Quebra o loop do menu

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.") #Retorna para o usuário erro caso selecione opção não existente no menu

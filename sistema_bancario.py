menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

saldo = 0
deposito = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        deposito = float(input('Quanto você quer depositar? R$'))

        if deposito > 0:
            saldo = saldo + deposito
            print(f'Saldo: R${saldo}')
            extrato += (f'\nDepósito: R$ {deposito:.2f}')
        else:
            print('Operação falou! Digite um valor válido!')

    elif opcao == '2':

        while True:
            if numero_saques >= LIMITE_SAQUES:
                print('Limite máximo de saques realizados por dia')
                break

            saque = float(input('Quanto você quer sacar? R$'))

            if saque > saldo:
                print('Não foi possível sacar esse valor, pois não tem saldo dísponivel!')
                break

            if saque >= 500:
                print('Você só pode sacar no máximo R$500,00 reais por saque!')
                break

            if saque > 0:
                if saque > 0 and deposito == 0:
                    break
                else:
                    saldo = saldo - saque
                    extrato += (f'\nSaque: R$ -{saque}')
                    print(f'Saldo: R${saldo}')
                    numero_saques += 1
                    break
            else:
                print('Valor informado inválido!')
    elif opcao == '3':
        print('=================EXTRATO=================')
        print('Não foram realizados movimentações em sua conta.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('=========================================')

    elif opcao == '4':
        print('Saindo...')
        break
    else:
        print('Operação inválida, por favor digite novamente.')
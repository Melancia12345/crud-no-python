contas = []


def criar():

    try:

        nome = input("insira seu nome: ")
        senha = input("insira uma senha de seis digitos: ")
        nomeconta = input("digite o nome da sua conta: ")

        if nome.isalpha() and len(senha) >= 6 and len(nomeconta) >= 3:

            conta = {
                "nome": nome,
                "senha": senha,
                "nomeconta": nomeconta,
                "saldo": 100
            }

            contas.append(conta)

            print("conta criada")

        else:

            print("nome ou senha invalida")

    except ValueError:

        print("dados incorretos")


def depositar():

    try:

        verificar = input("digite sua senha: ")
        verificar2 = input("digite seu nome: ")

        for i in contas:

            if i["senha"] == verificar and i["nome"] == verificar2:

                valor = float(input("deposite um valor na sua conta: "))

                i["saldo"] = i["saldo"] + valor

                print(str(valor) + " depositado na conta com sucesso!")

                return

        print("conta não encontrada")

    except ValueError:

        print("dados do deposito incorreto")


def sacar():

    try:

        verificar = input("digite sua senha: ")
        verificar2 = input("digite seu nome: ")

        for i in contas:

            if i["senha"] == verificar and i["nome"] == verificar2:

                valor = float(input("digite quanto voce quer sacar: "))

                if valor > i["saldo"]:

                    print("seu saldo é incompativel com o seu saque")

                else:

                    i["saldo"] = i["saldo"] - valor

                    print("seu saque de " + str(valor) + " foi sucedido!")

                return

        print("conta não encontrada")

    except ValueError:

        print("dados do saque incorreto")


def extrato():

    verificar = input("digite sua senha: ")
    verificar2 = input("digite seu nome: ")

    for i in contas:

        if i["senha"] == verificar and i["nome"] == verificar2:

            print("seu saldo bancario é " + str(i["saldo"]))

            return

    print("conta não encontrada")


while True:

    try:

        print("\nescolha uma opção:")
        print("1 criar conta")
        print("2 depositar")
        print("3 sacar")
        print("4 ver extrato")
        print("5 sair")

        escolha = int(input("faça sua escolha: "))

        if escolha == 1:

            criar()

        elif escolha == 2:

            depositar()

        elif escolha == 3:

            sacar()

        elif escolha == 4:

            extrato()

        elif escolha == 5:

            print("voce saiu")

            break

        else:

            print("não existe essa opção")

    except ValueError:

        print("valor invalido")
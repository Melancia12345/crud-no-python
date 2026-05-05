cadastro = []

def criar():
    try:
        nome = input("digite seu nome:")
        idade = int(input("digite sua idade:"))
        cidade = input("digite sua cidade")

        if nome.isalpha() and cidade.isalpha():
            login = {
                "Nome": nome,
                "Idade": idade,
                "Cidade": cidade
            }
            cadastro.append(login)
            print("Dados armazenados com sucesso!")
        else:
            print("Dados inválidos. Tente novamente.")
    except ValueError:
        print("dados inseridos incorretamente.")

def listar():
    if not cadastro:
        print("lista vazia")
    else:
        print("--- Cadastros ---")
        for i, pessoa in enumerate(cadastro):
            print(f"{i}: Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Cidade: {pessoa['Cidade']}")

def atualizar():
    listar()
    try:
        escolha = int(input("escolha um indice para mudar o cadastro"))
        if 0 <= escolha < len(cadastro):
            Nome = input("digite seu nome:")
            Idade = int(input("digite sua idade:"))
            Cidade = input("digite sua cidade")
            cadastro[escolha] = {
                "Nome": Nome,
                "Idade": Idade,
                "Cidade": Cidade
            }
            print("cadastro atualizado")
        else:
            print("cadastro inexistente")
    except ValueError:
        print("Entrada inválida.")

def excluir():
    listar()
    try:
        escolha = int(input("escolha um indice para excluir o cadastro"))
        if 0 <= escolha < len(cadastro):
            cadastro.pop(escolha)
            print("Cadastro excluído com sucesso!")
        else:
            print("Indice incorreto")
    except ValueError:
        print("Entrada inválida.")

while True:
    try:
        print("\nescolha uma opção")
        print("1 criar cadastro")
        print("2 listar o cadastro")
        print("3 mudar o cadastro")
        print("4 excluir o cadastro")
        print("5 sair")

        escolha = int(input("faça a escolha"))

        if escolha == 1:
            criar()
        elif escolha == 2:
            listar()
        elif escolha == 3:
            atualizar()
        elif escolha == 4:
            excluir()
        elif escolha == 5:
            print("encerrando...")
            break
        else:
            print("escolha invalida")

    except ValueError:
        print("Entrada inválida.")
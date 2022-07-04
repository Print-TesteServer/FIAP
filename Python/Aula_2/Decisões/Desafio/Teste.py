nivel=input("Digite o nível de acesso: ").upper()
sexo = (input("Digite seu gênero: ")).upper()

if nivel=="ADM" or nivel=="USR":
    if nivel=="ADM":
        if sexo == "MASCULINO":
            print("Olá Administrador")
        elif sexo == "FEMININO":
            print("Olá Administradora")

    else:
        if sexo == "MASCULINO":
            print("Olá Usuário")
        elif sexo == "FEMININO":
            print("Olá Usuária")

if nivel=="GUEST":
    print("Olá Visitante")

else:
    print("Olá Desconhecido")
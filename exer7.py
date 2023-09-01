def nome_e_sobrenome(nome):
    partes_nome = nome.split()
    nome_usuario = partes_nome[0]
    sobrenome_usuario = " ".join(partes_nome[1])
    nome_completo = nome.upper ( )
    tamanho_nome_completo = len(nome)

    print("nome: "+nome_completo.lower())
    print("tem ",tamanho_nome_completo, " caracteres ")

nome_e_sobrenome(input("Digite seu nome completo "))

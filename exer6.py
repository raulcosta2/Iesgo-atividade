def nome_sobrenome():
    nome = input("digite seu nome completo ")
    pats_nome = nome.split()
    primeiro_nome = pats_nome[0]
    sobrenome = "".join(pats_nome[1])

    return primeiro_nome.upper() +""+ sobrenome.lower()
print(nome_sobrenome())

    

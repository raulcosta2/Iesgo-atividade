def cont_de_a():
    nome = input("Digite seu nome completo ")
    return f"A letra 'a' aparece {nome.count('a')+nome.count('A')} vezes"

print(cont_de_a())
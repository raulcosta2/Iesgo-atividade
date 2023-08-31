def substituir_vogal():
    frase = input("digite uma frase")
    return frase.replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('u','*')
print(substituir_vogal())

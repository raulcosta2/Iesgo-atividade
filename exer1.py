def substituir_vogal():
    frase = input("digite uma frase")
    return frase.replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('u','*').replace('A','*').replace('E','*').replace('I','*').replace('O','*').replace('U','*')
print(substituir_vogal())

def apagar():
    vogal = input("Digite uma vogal ")
    return vogal.replace("a","").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")

print(apagar())
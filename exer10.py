def quantidade_caracter(texto):
    texto_sem_espaca = texto.lower().replace(' ', '')
    return len(texto_sem_espaca)
 
    
print("esse texto tem ",quantidade_caracter(input("Digite texto ")), " caracteres ")
s = "Jogo da Forca"
print(65*"=")
print(s.center(65,"="))
print(65*"=")
dica = input("Digite a dica:").lower().strip()
palavra = input("Digite a palavra secreta:").lower().strip()
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    print("A dica é:",dica)
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Parabéns você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("x==:==\nx  :  ")
    print("x  0  " if erros >= 1 else "x")
    linha2=""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros >= 4:
        linha2 = " \|/ "
    print("x%s" % linha2)
    linha3 =""
    if erros == 5:
        linha3 += " /   "
    elif erros >=6:
        linha3 += " / \ "
    print("x%s" % linha3)
    print("x\n===========")
    if erros == 6:
        print("Enforcado!")
        print("A palavra era:",palavra)
        break

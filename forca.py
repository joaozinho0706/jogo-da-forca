def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "Framboesa"
    letras_acertadas = ["_","_","_", "_","_","_","_","_","_"]

    enforcou = False
    acertou =  False
    
    while (not enforcou and not acertou):
        chute = input("Qual é a letra?")
        chute = chute.strip()
        
        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
            posicao = posicao + 1
        
        
        print(letras_acertadas)
    
    

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()


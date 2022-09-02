import random, os

def limpar():
    os.system('cls')
def ppt(pontos_maquina = 0, pontos_pessoa = 0):


    tupla = ("pedra", "papel", "tesoura")

    r1 = (random.choice(tupla))
    #print(r1)

    print("pedra, papel ou tesoura?")
    r2 = input("Digite: ")


    #opções da maquina vencendo

    if r1 == r2:
        limpar()
        print("Empate")


    elif r1 == "pedra" and r2 == "tesoura":
        limpar()
        print("A maquina venceu!")
        pontos_maquina = pontos_maquina + 1

    elif r1 == "tesoura" and r2 == "papel":
        limpar()
        print("A maquina venceu!")
        pontos_maquina = pontos_maquina + 1

    elif r1 == "papel" and r2 == "pedra":
        limpar()
        print("A maquina venceu!")
        pontos_maquina = pontos_maquina + 1

    else:
        pass

    #opções da pessoa vencendo

    if r1 == "pedra" and r2 == "papel":
        limpar()
        print("Você venceu!")
        pontos_pessoa = pontos_pessoa + 1

    elif r1 == "tesoura" and r2 == "pedra":
        limpar()
        print("Você venceu!")
        pontos_pessoa = pontos_pessoa + 1

    elif r1 == "papel" and r2 == "tesoura":
        limpar()
        print("Você venceu!")
        pontos_pessoa = pontos_pessoa + 1

    else:
        pass

    print('\n', 'Maquina:', r1, 'vs','Você:', r2, '\n')



while True:
    ppt()

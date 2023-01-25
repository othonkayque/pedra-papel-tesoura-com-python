import random, os, pyfiglet

def limpar():
    os.system('cls')
def ppt(pontos_maquina = 0, pontos_pessoa = 0):


    tupla = ("pedra", "papel", "tesoura")

    r1 = (random.choice(tupla))
    #print(r1)

    print("\n1 - pedra \n2 - papel \n3 - tesoura")
    r2 = input("Digite: ")

    #resultados com pyfiglet

    def empate():
        print(pyfiglet.figlet_format("Empate"))
    
    def venceu():
        print(pyfiglet.figlet_format("Venceu"))

    def perdeu():
        print(pyfiglet.figlet_format("Perdeu"))

    #opções da maquina vencendo

    if r1 == r2:
        limpar()
        empate()


    elif r1 == "pedra" and r2 == "tesoura" or r1 == "pedra" and r2 == "3":
        limpar()
        perdeu()
        pontos_maquina = pontos_maquina + 1

    elif r1 == "tesoura" and r2 == "papel" or r1 == "tesoura" and r2 == "2":
        limpar()
        perdeu()
        pontos_maquina = pontos_maquina + 1

    elif r1 == "papel" and r2 == "pedra" or r1 == "papel" and r2 == "1":
        limpar()
        perdeu()
        pontos_maquina = pontos_maquina + 1

    else:
        pass

    #opções da pessoa vencendo

    if r1 == "pedra" and r2 == "papel" or r1 == "pedra" and r2 == "2":
        limpar()
        venceu()
        pontos_pessoa = pontos_pessoa + 1

    elif r1 == "tesoura" and r2 == "pedra" or r1 == "tesoura" and r2 == "1":
        limpar()
        venceu()
        pontos_pessoa = pontos_pessoa + 1

    elif r1 == "papel" and r2 == "tesoura" or r1 == "papel" and r2 == "3":
        limpar()
        venceu()
        pontos_pessoa = pontos_pessoa + 1

    else:
        pass

    print('\n', 'Maquina:', r1, 'vs','Você:', r2, '\n')



while True:
    ppt()

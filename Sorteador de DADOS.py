import random
import time

def dado():
    dado = random.randint(1, 6)
    return dado
def um_dado():
    lançamento = dado ()
    print("Dado Número: {}".format(lançamento))

def dois_dados():
    dados1 = dado()
    print("Dado Número 1: {}".format(dados1))
    dados2 = dado()
    soma = dados1 + dados2
    print("Dado Número 2: {}".format(dados2))
    print("\n A soma dos dois dados é de: {}".format(soma))

def varias_jogadas():
    while True:
        numero_jogadas = int(input("Quantas vezes queres jogar: "))
        print("\n")
        contar = 1
        soma = 0
        try:
            while numero_jogadas >= contar:
                dados = dado()
                print("Jogada {}: {} ".format(contar,dados))
                contar = contar + 1
                soma = soma + dados
            break
        except ValueError:
            print
            ("Desculpe, {} não é um número válido, tente de novo".format(numero_jogadas))
    print("\nA soma da jogada dos dados é de {}".format(soma))


def sair ():
    print("\t\t***********************")
    print("\t\t    Fim Do Programa")
    print("\t\t***********************\n")
    quit()

def menu():
    print("\n\t\t************************************"
          "\n\t\t\t  Menu Principal"
          "\n\t\t************************************")
    escolha = input(""" 
                A: Simulador de um dado
                B: Simulador de dois dados
                C: Simulador de várias jornadas
                D: Sair\n
                Escolha uma hipótese: """)
    escolha = escolha.lower()
    if escolha == 'a':
        um_dado()
        time.sleep(5)
        menu()
    elif escolha == 'b':
        dois_dados()
        time.sleep(5)
        menu()
    elif escolha == 'c':
        varias_jogadas()
        time.sleep(5)
        menu()

    elif escolha == 'd':
        time.sleep(5)
        sair()
    else:
        print("Erro na Tecla!")
        print("Por favor, escolha novamente.")
        menu()

menu()
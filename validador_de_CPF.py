import random
import os
sair = "N"

def menu():
    os.system("cls")
    print("Validador/Gerador de CPF")
    print("------------------------")
    x = input("  [V]alidar [G]erar: ")
    os.system("cls")
    return x.upper()
    
def aleatorio():
    cpf = ""
    for i in range(9):
        cpf += str(random.randint(0,9))
    return cpf

def cpf(cpf):
    while True:
        cpfFormatado = cpf.replace(".", "")
        cpfFormatado = cpfFormatado.replace("-", "")
        if cpfFormatado.isdigit():
            return cpfFormatado
        else:
            print("Formato de cpf invalido, insira novamente.")
            continue


def gerarPrimeiroDigito(cpf):
    soma = 0
    multiplicador = 10
    for i in range(9):
        numero = int(cpf[i])
        soma += numero * multiplicador
        multiplicador -= 1
    digito = soma * 10 % 11
    digito = digito if digito <=9 else 0
    cpfPrimeiroDigito = cpf[0:9] + f"{digito}"
    return cpfPrimeiroDigito

def gerarSegundoDigito(cpf):
    soma = 0
    multiplicador = 11
    for i in range(10):
        numero = int(cpf[i])
        soma += numero * multiplicador
        multiplicador -= 1
    digito = soma * 10 % 11
    digito = digito if digito <=9 else 0
    cpfSegundoDigito = cpf[0:10] + f"{digito}"
    return cpfSegundoDigito

def validador(x, y):
    if x == y:
        return print("Este CPF é valido")
    else:
        return print("Este CPF não é valido")

while sair != "S":
    sel = menu()
    if sel == "V":
        cpfInserido = input("Digite o cpf: ")
        x = cpf(cpfInserido)
        y = gerarSegundoDigito(gerarPrimeiroDigito(x))
        validador(x, y)
    elif sel == "G":

        x = cpf(aleatorio())
        y = gerarSegundoDigito(gerarPrimeiroDigito(x))
        print(y)

    sair = input("Deseja sair: [S]im / [N]ão: ").upper()
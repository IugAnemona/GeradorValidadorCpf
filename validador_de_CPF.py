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
    
    cpfFormatado = cpf.replace(".", "")
    cpfFormatado = cpfFormatado.replace("-", "")
    if cpfFormatado.isdigit():
        return cpfFormatado
    else:
         return None


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
    return gerarSegundoDigito(cpfPrimeiroDigito)
    

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
    x = None

    if sel == "V":
        while x is None:
            cpfInserido = input("Digite o cpf: ")
            x = cpf(cpfInserido)
            if x == None:
                print("Formato de cpf invalido")
        y = gerarPrimeiroDigito(x)
        validador(x, y)
    elif sel == "G":

        x = cpf(aleatorio())
        y = gerarPrimeiroDigito(x)
        print(y)

    sair = input("Deseja sair: [S]im / [N]ão: ").upper()
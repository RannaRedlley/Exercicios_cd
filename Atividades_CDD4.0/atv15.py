resp="s"
while resp =="s":
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))
    if v1 > v2:
        print(f"{v1},{v2}")
    elif v2 > v1:
        print(f"{v2},{v1}")
    else:
        print("Digite um número sem ser 0: ")

    resp=input("Deseja recomeçar o codigo? s/n: ")
print("Fechando o programa!")
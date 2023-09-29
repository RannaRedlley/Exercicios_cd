soma=0
repet = int(input("Digite a quantidade de números que deseja: "))
for x in range(repet):
    soma += float(input(f"Digite o {x}º valor: "))

final= soma/repet
print(f"A média {final}")
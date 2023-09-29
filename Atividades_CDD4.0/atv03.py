mesatual = int(input("Digite o mes atual: "))
anoatual = int(input("Digite o ano atual: "))
idade = int(input("Digite sua idade: "))
mesniver = int(input("Digite o mes que nasceu: "))
calculo = anoatual-idade
if mesniver>mesatual:
    print(f"O ano que vc nasceu: {calculo-1}")
else:
    print(f"O ano que vc nasceu: {calculo}")
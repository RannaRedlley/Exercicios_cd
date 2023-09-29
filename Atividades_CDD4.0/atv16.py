inicio = int(input("Que horas o Xadrez começou?: "))
fim = int(input("Que horas o Xadrez acabou?: "))

if inicio <= fim:
    total = inicio-fim
else:
    total=(240-inicio)+fim
print(f"A partida durou {total} horas")
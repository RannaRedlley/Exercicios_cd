num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro  número: "))

if num1 > num2:
    if num1 > num3:
        print(f"O {num1} e maior ")
elif num2 > num3:
    print(f"O {num2} e maior ")
else:
    print(f"O {num3} e maior")


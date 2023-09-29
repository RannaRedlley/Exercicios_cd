while True:6
num=int(input("Digite um número: "))
opcao=int(input("Qual a sua opção 1 para antecessor 2 para sucessor"))
if opcao == 1:
    print(num-1)
else:
    print(num+1)

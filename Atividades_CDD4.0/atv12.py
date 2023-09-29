eleitores = int(input("Digite o número de eleitores: "))
branco = int(input("Digite a quantidade de votos brancos: "))
nulos = int(input("Digite a quantidade de votos nulos: "))
validos = int(input("Digite a quantidade de votos validos: "))

branco = branco/eleitores*100
nulos = nulos/eleitores*100
validos = validos/eleitores*100

print(f"A quantidade de eleitores foi {eleitores} é a quantidade de pessoas que votaram nulo foi de {nulos}%")
print(f"A quantidade de votos em brancos foi de: {branco}%. A quantidade de pessoas validas foi de: {validos}%")
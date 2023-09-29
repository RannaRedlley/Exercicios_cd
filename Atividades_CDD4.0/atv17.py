maca = int(input("A maça custa R$ 1,30 Digite quantas maças você deseja: "))

if maca < 12:
    valorfinal=maca*1.30
    print(f"O custo total foi de: {valorfinal}")
elif maca > 12:
    valorfinal=maca+1
    print(f"O Custo total foi de {maca}")
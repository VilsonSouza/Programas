
ordem = int(input("Qual a ordem da matriz: "))


mat: int = [[0 for x in range(ordem)] for x in range(ordem)]

quant = 0
for i in range(0,ordem):
    for j in range(0,ordem):
        mat[i][j]= int(input(f"Elemento:[{i},{j}]"))
        if mat[i][j]<0:
            quant = quant+1

print("DIagonal Principal:")
for i in range(0,ordem):
    print(mat[i][i])

print(f"Quantidade de negativos: {quant}")
    



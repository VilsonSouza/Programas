

n: int
num:int
soma:int

n = int(input("Quantos numeros serao digitados? "))

soma=0
for i in range(0,n):
    num = int(input("Digite um numero: "))
    soma+=num

print(soma) 


n: int
soma: float
cont: int

n = int(input("Quantos numeros voce vai digitar? "))

vet:int = [0 for x in range(n)]

soma = 0
cont=0
for i in range(0,n):
    vet[i] = float(input("Digite um numero: "))
    soma = soma+vet[i]
    cont = cont+1

media = soma/cont

print("Valores:")
for i in range(0,n):
    print(vet[i])

print(f"Soma: {soma:.2f}")
print(f"Media: {media:.2f}")
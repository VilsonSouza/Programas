
n: int

n = int(input("Quantos numeros voce vai digitar? "))

vet:int = [0 for x in range(n)]

for i in range(0,n):
    vet[i] = float(input("Digite um numero: "))

print("Numeros digitados: ")

for i in range(0,n):
        print(f"{vet[i]:.1f}")


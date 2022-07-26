print("Digite dois numeros: ")
num1 = int(input())
num2 = int(input())


i =0
soma=0
if num1<num2:
    for i in range(num1,num2):
        if i %2 == 1:
            soma = soma+i
        elif i<0:
            break;
    print(f"Soma dos impares: {soma}")

else:
    for i in range(num2,num1):
        if i %2 == 1:
            soma = soma+i
        elif i<0:
            break;
    print(f"Soma dos impares: {soma}")


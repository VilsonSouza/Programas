print("Digite dois numeros:")
num1 = int(input())
num2 = int(input())

if num1<num2:
    print("Crescente")
else :
    print("Decrescente")
while num1 != num2:
    print("Digite outros dois numeros:")
    num1 = int(input())
    num2 = int(input())
    if num1<num2:
        print("Crescente")
    elif num1>num2:
        print("Decrescente")
    if num1 == num2:
        break;

    
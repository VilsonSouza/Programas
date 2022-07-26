
num1 = int(input("Primeiro valor: "))

num2 = int(input("Segundo valor: "))

num3 = int(input("Terceiro valor: "))

if num1<num2 and num2<num3:
    print(f"Menor: {num1}")
elif num2<num1 and num1<num3:
    print(f"Menor: {num2}")
elif num3<num1 and num1<num2:
    print(f"Menor: {num3}")

if num1== num2 and num1<num3:
    print(f"Menor: {num1}")
elif num2 == num3 and num2<num1:
    print(f"Menor: {num2}")
elif num3 == num2 and num3<num1:
    print(f"Menor: {num3}")
elif num1 == num3 and num1<num2:
    print(f"Menor: {num1}")

elif num1==num2 and num2 == num3:
    print(f"Menor: {num1}")
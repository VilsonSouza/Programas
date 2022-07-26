
print("Dados da primeira pessoa: ")
nome = input("Nome: ")
idade = int(input("Idade: "))

print("Dados da segunda pessoa: ")
nome2= input("Nome: ")
idade2 = int(input("Idade: "))

media = float(idade+idade2)/2

print(f"A idade media de {nome} e {nome2} eh de {media:.1f}")

num: int
soma: int

soma=0
num= int(input("Insira um numero: "))
soma+=num

while num != 0:
    soma +=num
    num= int(input("Insira outro numero: "))
  

print(soma)

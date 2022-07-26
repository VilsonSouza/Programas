import math

base = float(input("Base do retangulo:"))
altura= float(input("Altura do retangulo: "))

area = base*altura
perimetro = 2*(base+altura)
diagonal = math.sqrt((base**2)+(altura**2))

print(f"area: {area:.4f}")
print(f"Perimetro: {perimetro:.4f}")
print(f"diagonal: {diagonal:.4f}")
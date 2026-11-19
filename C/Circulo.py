import math

radio = float(input("Radio del círculo: "))

area = math.pi * math.pow(radio, 2)
perimetro = 2 * math.pi * radio

print("Area:", round(area, 2))
print("Perímetro:", round(perimetro, 2))
print("Raiz cuadrada del área:", round(math.sqrt(radio), 2))
print("techo del area:", math.ceil(area))

x = 3
y = 2
pow=math.pow(x, y)
print("x,y",math.pow(x, y))

x = 2
log = math.log(x, 2)
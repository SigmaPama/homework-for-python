import math
def square(side):
    return math.ceil (side*side)

side = int(input("Чему равна сторона? "))
print(f"Площадь квадрата = {square(side)}")


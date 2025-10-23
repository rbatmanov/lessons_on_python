import math
def square(side_length):
    side_length_rounded = math.ceil(side_length)
    area = side_length_rounded ** 2
    return area
side = float(input("Введите сторону квадрата: "))
area = square(side)
print(f"Площадь квадрата со стороной {side} равна {area}")
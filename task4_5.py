import functools

print(f"Произведение всех элементов списка: {functools.reduce((lambda prev_el, el : prev_el * el), [el for el in range(100, 1001) if (el % 2 == 0)])}")
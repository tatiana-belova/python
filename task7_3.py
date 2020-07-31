class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return f'{self.cells}'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return Cell(self.cells - other.cells if self.cells > other.cells else other.cells - self.cells)

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, _count):
        cells_list = list('*' for i in range(self.cells))
        result = []
        a = 1
        for i in range(len(cells_list)):
            if a == _count:
                result.append(cells_list[i] + '\n')
                a = 1
            else:
                result.append(cells_list[i])
                a += 1
        return ''.join(result)


cell_1 = Cell(8)
cell_2 = Cell(33)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(cell_1.make_order(5))
print(cell_2.make_order(12))
class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __add__(self):
        mtrx = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list1)):

            for j in range(len(self.list2[i])):
                mtrx[i][j] = self.list1[i][j] + self.list2[i][j]

        return str("\n".join(["\t".join([str(j) for j in i]) for i in mtrx]))

    def __str__(self):
        return str("\n".join(["\t".join([str(j) for j in i]) for i in mtrx]))


new_matrix = Matrix([[3, 5, 32],
                     [2, 4, 6],
                     [-1, 64, -8]],
                    [[3, 5, 8],
                     [3, 8, 3],
                     [7, 1, 31]])

print(new_matrix.__add__())

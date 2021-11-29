class Matrix:
    def __init__(self, m, n):
        self.matrix = [[0 for i in range(n)] for i in range(m)]

    def __eq__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            return True
        else:
            return False

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            tableC = Matrix(len(self.matrix), len(self.matrix))
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    tableC.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return tableC

    def __sub__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            tableC = Matrix(len(self.matrix), len(self.matrix))
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    tableC.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return tableC

    def __mul__(self, other):
        if isinstance(other, int):
            tableC = Matrix(len(self.matrix), len(self.matrix[0]))
            for i in range(len(tableC.matrix)):
                for j in range(len(tableC.matrix[i])):
                    tableC.matrix[i][j] = self.matrix[i][j] * other
            return tableC
        if isinstance(other, Matrix):
            if len(self.matrix) == len(other.matrix[0]):
                tableC = Matrix(len(self.matrix[0]), len(other.matrix))
                for i in range(len(tableC.matrix)):
                    for j in range(len(tableC.matrix[i])):
                        for k in range(len(self.matrix[i])):
                            tableC.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                return tableC

    def __rmul__(self, other):
        return self.__mul__(other)

    def set_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = int(input())

    def __str__(self):
        matrix = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix += str(self.matrix[i][j]) + " "
            matrix += "\n"
        return matrix


macierz = Matrix(2, 2)
macierz.set_matrix()
macierzDwa = Matrix(2, 2)
macierzDwa.set_matrix()
print(macierz + macierzDwa)
print(macierz - macierzDwa)
print(macierz * macierzDwa)
print(macierz * 3)
print(3 * macierz)

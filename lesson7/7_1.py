class Matrix:
    def __init__(self, new_list):
        self.list = new_list

    def __str__(self):
        return '\n'.join([' '.join(map(str, i)) for i in self.list])

    def __add__(self, other):
        for i in range(len(self.list)):
            for j in range(len(other.list[i])):
                self.list[i][j] = self.list[i][j] + other.list[i][j]
        return Matrix.__str__(self)


m1 = Matrix([[1, 1, 1], [1, 0, 3]])
m2 = Matrix([[6, 6, 6], [2, 3, 2]])


print(m1)

print(m2)

print('сумма \n', m1+m2)

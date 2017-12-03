from collections import defaultdict

def dimension(n):
    m = 0
    while n > (2 * m + 1)**2:
        m += 1
    return 2 * m + 1


def elm(row, col):
    max_rowcol = max(abs(row), abs(col))
    dim = max_rowcol * 2 + 1
    if row == -max_rowcol:
        return dim**2 - (max_rowcol - col)
    elif col == -max_rowcol:
        return dim**2 - dim - (max_rowcol + row) + 1
    elif row == max_rowcol:
        return dim**2 - 2 * dim + 2 - (max_rowcol + col)
    return dim**2 - 3 * dim + 3 - (max_rowcol - row)


def pos(idx):
    dim = dimension(idx)
    max_rowcol = (dim - 1) / 2
    bottom_left = dim**2 - dim + 1
    top_left = dim**2 - 2 * dim + 2
    top_right = dim**2 - 3 * dim + 3
    if idx >= bottom_left:
        return (-max_rowcol, max_rowcol - (dim**2 - idx))
    elif idx >= top_left:
        return (-max_rowcol + (bottom_left - idx), -max_rowcol)
    elif idx >= top_right:
        return (max_rowcol, -max_rowcol + (top_left - idx))
    return (max_rowcol - (top_right - idx), max_rowcol)


def adjacents(position):
    (a, b) = position
    return [(a + i, b + j) for i in range(-1, 2) for j in range(-1, 2)]


def walk(destination):
    matrix = defaultdict(lambda: 0)
    matrix[(0, 0)] = 1
    n = 1
    while matrix[pos(n)] <= destination:
        n += 1
        n_pos = pos(n)
        elements = [matrix[p] for p in adjacents(pos(n))]
        result = sum(elements)
        matrix[pos(n)] = result
    return matrix[pos(n)]

# print(pos(22))
# print(elm(*pos(22)))
# print([pos(n) for n in [2,3,4,6,8]])
# print([elm(*pos(n)) for n in [2,3,4,6,8]])
print(walk(368078))


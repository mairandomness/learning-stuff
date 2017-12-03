def dimension(n):
    m = 0
    while n > (2*m+1)**2:
        m += 1
    return 2*m+1

def pos(n):
    dim = dimension(n)
    last_line = dim**2 - (dim-1)
    first_column = (dim - 1)**2 + 1
    first_line = (dim - 2)**2 + (dim - 1)
    last_column = (dim - 2)**2 + (dim - 1)
    # print(dict(n=n, dim=dim, last_line=last_line, first_column=first_column, first_line=first_line, last_column=last_column))
    if n >= last_line:
        return (dim-1, n - last_line)
    elif n >= first_column:
        return (n - first_column, 0)
    elif n >= first_line:
        return (0, n - first_line)
    return (last_column - n, dim - 1)

def distance(n):
    dim = dimension(n)
    pos1 = (dim-1)/2
    (a,b) = pos(n)
    return abs(a-pos1) + abs(b-pos1)

print(pos(22))
print(pos(17))
print(pos(4))
print(pos(6))
print(pos(8))
print(pos(2))
print(pos(368078))
print(distance(1))
print(distance(12))
print(distance(23))
print(distance(1024))
print(distance(368078))

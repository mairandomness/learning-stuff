
"""--- Part Two ---

How many pixels stay on after 18 iterations?"""
import numpy as np
from functools import reduce

def count_hashes(matrix):
    return matrix.sum()

def tomatrix(lst_of_str):
    matrixes = []
    for elem in lst_of_str:
        split = elem.split("/")
        matrixes.append(np.array([[ int(char) for char in row]for row in split]))
    return matrixes

def breakapart(matrix, sublen):
    row,col = (0,0)
    n = len(matrix)//sublen # num of submatrixes
    subs = [[] for i in range(n)]

    for row in range(0,len(matrix),sublen):
        for col in range(0,len(matrix),sublen):
            subs[row//sublen].append(matrix[row:row+sublen,col:col+sublen])
    return subs

def rejoin(subs):
    rowlist = []
    for row in subs:
        currow = row[0]
        for col in row[1:]:
            currow = np.concatenate((currow, col), axis=1)
        rowlist.append(currow)

    matrix = rowlist[0]
    for row in rowlist[1:]:
        matrix = np.concatenate((matrix, row), axis=0)

    return matrix

def id(x):
    return x

def tp(x):
    return x.T

def f0(x):
    return np.flip(x, axis=0)

def f1(x):
    return np.flip(x, axis=1)

def matches(a,b):
    ops = [
        [id],[tp,f0],
        [tp],[tp,f1],
        [f0],[f0,f1],
        [f1],[tp,f0,f1],
    ]

    for opsequence in ops:
        a1 = reduce((lambda val,op: op(val)), opsequence, a)
        if np.all(a1 == b):
            return True

    return False

def transform(m, enhancements):
    for e, t in enhancements:
        if e.sum() == m.sum() and matches(m, e):
            return t
    print("vish, didnt match")

def main():
    f = open("input", "r")
    text = f.read()[:-1].replace(".", "0").replace("#","1").split("\n")
    enhancements = [tomatrix(line.split(" => ")) for line in text]

    initial = np.array([[0,1,0], [0,0,1], [1,1,1]])

    for i in range(18):
        if len(initial) % 2 == 0:
            subs = breakapart(initial, 2)
        else:
            subs = breakapart(initial, 3)

        subs = [[transform(col, enhancements) for col in row] for row in subs]

        initial = rejoin(subs)


    print(count_hashes(initial))

if __name__ == "__main__":
    main()

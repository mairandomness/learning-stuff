
"""--- Day 21: Fractal Art ---

You find a program trying to generate some art. It uses a strange process that involves repeatedly enhancing the detail of an image through a set of rules.

The image consists of a two-dimensional square grid of pixels that are either on (#) or off (.). The program always begins with this pattern:

.#.
..#
###
Because the pattern is both 3 pixels wide and 3 pixels tall, it is said to have a size of 3.

Then, the program repeats the following process:

If the size is evenly divisible by 2, break the pixels up into 2x2 squares, and convert each 2x2 square into a 3x3 square by following the corresponding enhancement rule.
Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3 squares, and convert each 3x3 square into a 4x4 square by following the corresponding enhancement rule.
Because each square of pixels is replaced by a larger one, the image gains pixels and so its size increases.

The artist's book of enhancement rules is nearby (your puzzle input); however, it seems to be missing rules. The artist explains that sometimes, one must rotate or flip the input pattern to find a match. (Never rotate or flip the output pattern, though.) Each pattern is written concisely: rows are listed as single units, ordered top-down, and separated by slashes. For example, the following rules correspond to the adjacent patterns:

../.#  =  ..
          .#

                .#.
.#./..#/###  =  ..#
                ###

                        #..#
#..#/..../#..#/.##.  =  ....
                        #..#
                        .##.
When searching for a rule to use, rotate and flip the pattern as necessary. For example, all of the following patterns match the same rule:

.#.   .#.   #..   ###
..#   #..   #.#   ..#
###   ###   ##.   .#.
Suppose the book contained the following two rules:

../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
As before, the program begins with this pattern:

.#.
..#
###
The size of the grid (3) is not divisible by 2, but it is divisible by 3. It divides evenly into a single square; the square matches the second rule, which produces:

#..#
....
....
#..#
The size of this enhanced grid (4) is evenly divisible by 2, so that rule is used. It divides evenly into four squares:

#.|.#
..|..
--+--
..|..
#.|.#
Each of these squares matches the same rule (../.# => ##./#../...), three of which require some flipping and rotation to line up with the rule. The output for the rule is the same in all four cases:

##.|##.
#..|#..
...|...
---+---
##.|##.
#..|#..
...|...
Finally, the squares are joined into a new grid:

##.##.
#..#..
......
##.##.
#..#..
......
Thus, after 2 iterations, the grid contains 12 pixels that are on.

How many pixels stay on after 5 iterations?

To begin, get your puzzle input."""
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
        if matches(m, e):
            return t
    print("vish, didnt match")

def main():
    f = open("input", "r")
    text = f.read()[:-1].replace(".", "0").replace("#","1").split("\n")
    enhancements = [tomatrix(line.split(" => ")) for line in text]

    initial = np.array([[0,1,0], [0,0,1], [1,1,1]])

    for i in range(5):
        if len(initial) % 2 == 0:
            subs = breakapart(initial, 2)
        else:
            subs = breakapart(initial, 3)

        subs = [[transform(col, enhancements) for col in row] for row in subs]

        initial = rejoin(subs)


    print(count_hashes(initial))

if __name__ == "__main__":
    main()

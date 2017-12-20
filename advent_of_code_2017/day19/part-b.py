"""
--- Part Two ---

The packet is curious how many steps it needs to go.

For example, using the same routing diagram from the example above...

     |
     |  +--+
     A  |  C
 F---|--|-E---+
     |  |  |  D
     +B-+  +--+

...the packet would go:

6 steps down (including the first line at the top of the diagram).
3 steps right.
4 steps up.
3 steps right.
4 steps down.
3 steps right.
2 steps up.
13 steps left (including the F it stops on).
This would result in a total of 38 steps.

How many steps does the packet need to go?

"""


def main():
    f = open("input", "r")
    field = f.read()[:-1].split("\n")

    i = 0
    j = field[0].index("|")
    letters = []
    steps = 0

    di = 1
    dj = 0

    dict_dir = {"|" : [(1,0), (-1,0)],
                "-" : [(0,1), (0,-1)]}

    while field[i][j] != " " and 0<= i < len(field) and 0 <= j < len(field[i]):
        i += di
        j += dj
        if field[i][j].isalpha():
            letters.append(field[i][j])

        elif field[i][j] == "+":
            possible_neighbours = [[dj, di], [-dj, -di]]
            for neighbour in possible_neighbours:
                try:
                    char = field[i+neighbour[0]][j+neighbour[1]]
                except IndexError:
                    continue
                if char.isalpha() or char == "|" or char == "-":
                    di = neighbour[0]
                    dj = neighbour[1]
                    break
        steps +=1
    print(steps)







if __name__ == "__main__":
    main()

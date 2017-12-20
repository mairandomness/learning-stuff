"""--- Day 19: A Series of Tubes ---

Somehow, a network packet got lost and ended up here. It's trying to follow a routing diagram (your puzzle input), but it's confused about where to go.

Its starting point is just off the top of the diagram. Lines (drawn with |, -, and +) show the path it needs to take, starting by going down onto the only line connected to the top of the diagram. It needs to follow this path until it reaches the end (located somewhere within the diagram) and stop there.

Sometimes, the lines cross over each other; in these cases, it needs to continue going the same direction, and only turn left or right when there's no other option. In addition, someone has left letters on the line; these also don't change its direction, but it can use them to keep track of where it's been. For example:

     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+

Given this diagram, the packet needs to take the following path:

Starting at the only line touching the top of the diagram, it must go down, pass through A, and continue onward to the first +.
Travel right, up, and right, passing through B in the process.
Continue down (collecting C), right, and up (collecting D).
Finally, go all the way left through E and stopping at F.
Following the path to the end, the letters it sees on its path are ABCDEF.

The little packet looks up at you, hoping you can help it find the way. What letters will it see (in the order it would see them) if it follows the path? (The routing diagram is very wide; make sure you view it without line wrapping.)"""


def main():
    f = open("input", "r")
    field = f.read()[:-1].split("\n")

    i = 0
    j = field[0].index("|")
    letters = []


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
    print("".join(letters))







if __name__ == "__main__":
    main()

"""--- Part Two ---

Now, all the defragmenter needs to know is the number of regions. A region is a group of used squares that are all adjacent, not including diagonals. Every used square is in exactly one region: lone used squares form their own isolated regions, while several adjacent squares all count as a single region.

In the example above, the following nine regions are visible, each marked with a distinct digit:

11.2.3..-->
.1.2.3.4
....5.6.
7.8.55.9
.88.5...
88..5..8
.8...8..
88.8.88.-->
|      |
V      V
Of particular interest is the region marked 8; while it does not appear contiguous in this small view, all of the squares marked 8 are connected when considering the whole 128x128 grid. In total, in this example, 1242 regions are present.

How many regions are present given your key string?"""

import hashing as hs

def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(8)


def total_ones(binary_list):
    total = 0
    for line in binary_list:
        for char in line:
            if char == '1':
                total += 1
    return total

def find_adjecents(binary_list, i, j):
    binary_list[i][j] = '2'
    adjecent_coords = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
    for coord in adjecent_coords:
        (a, b) = coord
        if 0 <= a < len(binary_list) and 0 <= b < len(binary_list[0])  and binary_list[a][b] =='1':
            find_adjecents(binary_list, a,b)
    return binary_list


def main():
    input_str = "wenycdww"
    hex_list = []
    for i in range (0, 128):
        hex_list.append(hs.knot_hash(input_str + "-" + str(i)))
    binary_list = [[hex_to_bin(hex_str) for hex_str in line] for line in hex_list]
    binary_list = [list("".join(line)) for line in binary_list]
    print(binary_list)

    groups = 0
    #now to count the regions
    while total_ones(binary_list) > 0:
        for i in range(len(binary_list)):
            for j in range(len(binary_list[0])):
                if binary_list[i][j] == '1':
                    groups += 1
                    binary_list = find_adjecents(binary_list, i, j)
    print(groups)





if __name__ == "__main__":
    main()

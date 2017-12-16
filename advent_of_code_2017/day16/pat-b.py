"""--- Day 16: Permutation Promenade ---

You come upon a very unusual sight; a group of programs here appear to be dancing.

There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
Exchange, written xA/B, makes the programs at positions A and B swap places.
Partner, written pA/B, makes the programs named A and B swap places.
For example, with only five programs standing in a line (abcde), they could do the following dance:

s1, a spin of size 1: eabcd.
x3/4, swapping the last two programs: eabdc.
pe/b, swapping programs e and b: baedc.
After finishing their dance, the programs end up in order baedc.

You watch the dance for a while and record their dance moves (your puzzle input). In what order are the programs standing after their dance?"""

import pandas as pd

def spin(positions, num):
    positions = pd.concat([positions[-num:], positions[:len(positions) - num]])
    for i in range(len(positions)):
        positions.iloc[i] = i
    return positions

def exchange(positions, num_a, num_b):
    temp = positions.iloc[num_a]
    positions.iloc[num_a] = positions.iloc[num_b]
    positions.iloc[num_b] = temp
    return positions

def swap(positions, key_a, key_b):
    temp = positions.loc[key_a]
    positions.loc[key_a] = positions.loc[key_b]
    positions.loc[key_b] = temp
    return positions

def main():
    f = open("input", "r")
    text = f.read()[:-1]
    instruction_lines = text.split(",")
    instructions = []
    for line in instruction_lines:
        if len(line) > 3:
            new_line = [line[0], line[1:].split("/")]
            instructions.append(new_line)
        else:
            instructions.append(line)

    letters = "abcdefghijklmnop"
    positions_dict = {}
    for idx, key in enumerate(letters):
        positions_dict[key] = idx

    positions = pd.Series(positions_dict)
    history = {}

    for i in range(1000):
        for order in instructions:
            if order[0] == "s":
                positions = spin(positions, int(order[1:]))
            if order[0] == "x":
                positions = exchange(positions, int(order[1][0]), int(order[1][1]))
            if order[0] == "p":
                positions = swap(positions, order[1][0], order[1][1])
            positions = positions.sort_values()
        cur_str = "".join(list(positions.keys()))
        if cur_str not in history:
            history[cur_str] = i+1
        else:
            loop_size = i + 1 - history[cur_str]
            remainder = 1000000000 % loop_size
            for key in history:
                if history[key] == remainder:
                    print(key)
                    break
            break


if __name__ == "__main__":
    main()

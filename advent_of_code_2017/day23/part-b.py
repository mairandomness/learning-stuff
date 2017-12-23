
"""--- Day 23: Coprocessor Conflagration ---

You decide to head directly to the CPU and fix the printer from there. As you get close, you find an experimental coprocessor doing so much work that the local programs are afraid it will halt and catch fire. This would cause serious issues for the rest of the computer, so you head in and see what you can do.

The code it's running seems to be a variant of the kind you saw recently on that tablet. The general functionality seems very similar, but some of the instructions are different:

set X Y sets register X to the value of Y.
sub X Y decreases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
Only the instructions listed above are used. The eight registers here, named a through h, all start at 0.

The coprocessor is currently set to some kind of debug mode, which allows for testing, but prevents it from doing any meaningful work.

If you run the program (your puzzle input), how many times is the mul instruction invoked?"""

def main():
    f = open("input", "r")
    text = f.read()[:-1].split("\n")
    input_lst = [line.split(" ") for line in text]
    instructions = []

    for line in input_lst:
        new_line = []
        for char in line:
            if char.isalpha():
                new_line.append(char)

            else:
                new_line.append(int(char))

        instructions.append(new_line)

    keys = "abcdefgh"
    register = {}
    for key in keys:
        register[key] = 0
    register['a'] = 1
    i = 0

    while 0 <= i < len(instructions):
        func = instructions[i][0]
        var = instructions[i][1]
        value = instructions[i][2]
        print(register)
        print(i+1, instructions[i])
        input()
        # if var == 'c':
        #     continue
        if type(value) == str:
                value = register[value]

        if func == "set":
            register[var] = value

        elif func == "sub":
            register[var] -= value

        elif func == "mul":
            register[var] *= value

        elif func == "jnz":
            if type(var) == str:
                var = register[var]
            if var != 0:
                i += value
                continue
        i += 1

    print(register['h'])

if __name__ == "__main__":
    main()


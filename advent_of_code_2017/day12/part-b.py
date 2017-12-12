
"""--- Part Two ---

There are more programs than just the ones in the group containing program ID 0. The rest of them have no way of reaching that group, and still might have no way of reaching each other.

A group is a collection of programs that can all communicate via pipes either directly or indirectly. The programs you identified just a moment ago are all part of the same group. Now, they would like you to determine the total number of groups.

In the example above, there were 2 groups: one consisting of programs 0,2,3,4,5,6, and the other consisting solely of program 1.

How many groups are there in total?"""

def main():
    f = open("input", "r")

    text = f.read()[:-1]
    line_lst = text.split("\n")
    input_lst=[]
    for line in line_lst:
        input_lst.append(line.split(" <-> "))
    child_lst = []
    for line in input_lst:
        child_lst.append([int(elem) for elem in line[1].split(", ")])

    loops = 0
    checked_idxs = []

    for idx in range(len(child_lst)):
        if idx not in checked_idxs:
            checked = [][:]
            to_check = [idx]
            while len(to_check) > 0:
                for elem in child_lst[to_check[0]]:
                    if elem not in checked:
                        to_check.append(elem)

                if to_check[0] not in checked:
                    checked.append(to_check[0])
                to_check = to_check[1:]

            checked_idxs = checked_idxs[:] + checked[:]
            loops+=1

    print(len(checked_idxs)) #should be 2000
    print(loops)
if __name__=="__main__":
    main()


"""
--- Part Two ---

Out of curiosity, the debugger would also like to know the size of the loop: starting from a state that has already been seen, how many block redistribution cycles must be performed before that same state is seen again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the answer in that example would be 4.

How many cycles are in the infinite loop that arises from the configuration in your puzzle input?"""



def find_max(lst):
    max_elem = lst[0]
    max_idx = 0
    for i in range(0, len(lst)):
        if lst[i] > max_elem:
            max_elem = lst[i]
            max_idx = i
    return (max_idx, max_elem)


def update_lst(lst):
    len_lst = len(lst)
    (max_idx, max_elem) = find_max(lst)
    count = max_elem
    lst[max_idx] = 0
    idx = max_idx + 1
    while count > 0:
        if idx == len_lst:
            idx = 0
        lst[idx] += 1
        idx += 1
        count -= 1
    return lst


def main():
    input_str = "4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5"
    input_test = "0\t2\t7\t0"

    str_lst = input_str.split("\t")
    input_lst = []
    for elem in str_lst:
        input_lst.append(int(elem))
    pattern_lst = []
    pattern_lst.append(input_lst[:])
    count = 0
    while True:
        input_lst = update_lst(input_lst)
        if input_lst in pattern_lst:
            count += 1
            break
        else:
            pattern_lst.append(input_lst[:])
            count += 1
    print(count-pattern_lst.index(input_lst))


if __name__ == "__main__":
    main()

"""--- Part Two ---

The bridge you've built isn't long enough; you can't jump the rest of the way.

In the example above, there are two longest bridges:

0/2--2/2--2/3--3/4
0/2--2/2--2/3--3/5
Of them, the one which uses the 3/5 component is stronger; its strength is 0+2 + 2+2 + 2+3 + 3+5 = 19.

What is the strength of the longest bridge you can make? If you can make multiple bridges of the longest length, pick the strongest one."""
import copy
def get_next_lvl(cur_end, ports, cur_sum, cur_len):
    cur_sum += cur_end
    cur_len += 1
    if len(ports[cur_end]) > 0:
        cur_sum += cur_end
    else:
        return (cur_sum, cur_len)

    max_len_sum = 0
    max_len = 0

    for port in ports[cur_end]:
        ports_copy = copy.deepcopy(ports)
        ports_copy[cur_end].remove(port)
        if port != cur_end:
            ports_copy[port].remove(cur_end)

        (new_sum, new_len) = (get_next_lvl(port, ports_copy, cur_sum, cur_len))
        if new_len > max_len or (new_len == max_len and new_sum > max_len_sum):
            max_len = new_len
            max_len_sum = new_sum

    return (max_len_sum, max_len)




# def go_back_lvl():


def main():
    f = open("input", "r")
    text = f.read()[:-1].split("\n")
    text2 = [line.split("/") for line in text]
    text3 = [sorted([int(elem) for elem in line]) for line in text2]
    ports = {}
    for line in text3:
        if line[0] not in ports:
            ports[line[0]] = []
        if line[1] not in ports:
            ports[line[1]] = []
        ports[line[0]].append(line[1])
        if line[0] != line[1]:
            ports[line[1]].append(line[0])

    print(get_next_lvl(0,ports, 0,0))




    print(ports)





if __name__ == "__main__":
    main()

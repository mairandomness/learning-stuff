def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
    lines = text.split("\n")
    n_list = [line.split() for line in lines[1:]]
    tuple_list = [(int(w)-int(l), int(w), int(l)) for w, l in n_list]
    sorted_list = sorted(tuple_list, reverse=True)
    print(sorted_list)
    return sorted_list


def main():
    sorted_list = parse_input()

    comp_time = 0
    total = 0
    for process in sorted_list:
        comp_time += process[2]
        total += comp_time * process[1]

    print(total)


if __name__ == "__main__":
    main()

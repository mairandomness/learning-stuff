def parse_input():
    f = open("input.txt", "r")
    text = f.read()[:-1]
    lines = text.split("\n")
    return (lines)

def main():
    lines = parse_input()
    print(len(lines))
    print(len(set(lines)))


if __name__ == "__main__":
    main()

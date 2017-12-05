
def main():
    f = open("input", "r")
    text = f.read()
    str_lst = text.split("\n")[:-1]

    int_lst = []
    for elem in str_lst:
        int_lst.append(int(elem))
    i = 0
    count = 0
    while 0 <= i < len(int_lst):
        walk = int_lst[i]
        if int_lst[i] >= 3:
            int_lst[i] -= 1
        else:
            int_lst[i] += 1
        i += walk
        count+=1
    print(count)
if __name__ == "__main__":
    main()

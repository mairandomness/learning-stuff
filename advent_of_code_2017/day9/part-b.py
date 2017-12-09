""" --- Part Two ---

Now, you're ready to remove the garbage.

To prove you've removed it, you need to count all of the characters within the garbage. The leading and trailing < and > don't count, nor do any canceled characters or the ! doing the canceling.

<>, 0 characters.
<random characters>, 17 characters.
<<<<>, 3 characters.
<{!>}>, 2 characters.
<!!>, 0 characters.
<!!!>>, 0 characters.
<{o"i!a,<{i<a>, 10 characters.
How many non-canceled characters are within the garbage in your puzzle input? """


def main():
    f = open("input", "r")
    input_str = f.read()

    test3 = "<>"
    test4 = "<random characters>"
    test5 = "<<<<>"
    test6 = "<{!>}>"
    test7 = "<!!!>>"
    test8 = "<{o.i!a,<{i<a>"

    non_canceled_garb = 0
    ignore_until = False
    string = input_str
    i = 0
    while i < len(string):
        if ignore_until and string[i] == "!":
            i+=2
            continue
        elif ignore_until and string[i] != ">":
            i+=1
            non_canceled_garb += 1
            continue
        elif ignore_until and string[i] == ">":
            ignore_until = False

        elif string[i] == "<":
            ignore_until = True

        i+=1

    print(non_canceled_garb)


if __name__ == "__main__":
    main()


"""--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?"""


def check_condition(cond_list, values_dict):
    """ cond_list[0] is a possible key in dict
        cond_list[1] is the comparison >, <, ==, <=, >=
        cond_list[2] is the value to compare to (in str form)"""
    key = cond_list[0]
    compare_str = cond_list[1]
    number = int(cond_list[2])

    if key not in values_dict:
        values_dict[key] = 0
    if compare_str == ">":
        return values_dict[key] > number
    elif compare_str == "<":
        return values_dict[key] < number
    elif compare_str == ">=":
        return values_dict[key] >= number
    elif compare_str == "<=":
        return values_dict[key] <= number
    elif compare_str == "!=":
        return values_dict[key] != number
    return values_dict[key] == number

def execute_order(order_list, values_dict):
    key = order_list[0]
    operator = order_list[1]
    number = int(order_list[2])

    if key not in values_dict:
        values_dict[key] = 0
    if operator == "inc":
        values_dict[key] += number
    else:
        values_dict[key] -= number



def main():
    f=open("input", "r")
    text = f.read()
    str_list = text.split("\n")[:-1]
    str_list2 = [line.split(" if ") for line in str_list]
    str_list3 = []
    for line in str_list2:
        str_list3.append([elem.split(" ") for elem in line])
    values_dict = {}
    for line in str_list3:
        order_list = line[0]
        cond_list = line[1]
        if check_condition(cond_list, values_dict):
            execute_order(order_list, values_dict)

    maxvalue_key =max(values_dict, key = values_dict.get)
    print(maxvalue_key, values_dict[maxvalue_key] )




if __name__ == "__main__":
    main()


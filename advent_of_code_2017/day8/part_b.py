"""--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated)."""


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
    max_overall = 0
    for line in str_list3:
        order_list = line[0]
        cond_list = line[1]
        if check_condition(cond_list, values_dict):
            execute_order(order_list, values_dict)
            max_key =max(values_dict, key = values_dict.get)
            if max_overall < values_dict[max_key]:
                max_overall = values_dict[max_key]


    max_key =max(values_dict, key = values_dict.get)
    print(max_key, values_dict[max_key])
    print(max_overall)




if __name__ == "__main__":
    main()


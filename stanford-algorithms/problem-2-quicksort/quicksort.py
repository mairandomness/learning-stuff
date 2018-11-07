# import sys
# sys.setrecursionlimit(100000)

def quicksort(counter, input_list):
    smaller = []
    larger = []
    if len(input_list) > 1:
    # to implement one day in the future?
        return (counter, lst)
    else:
        return (0, input_list)



def parse_input():
    f = open("input", "r")
    text = f.read()[:-1]
    lines = text.split("\n")
    input_list = [int(number) for number in lines]
    return (input_list)

def main():
    input_list = parse_input()
    print(quicksort(0,input_list))

if __name__ == "__main__":
    main()

""" from day 10 partb"""

from functools import reduce
def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]


def knot_hash(input_str):
    input_lst = [ord(char) for char in input_str] + [17, 31, 73, 47, 23]
    #run 64 rounds, preserve cur_pos and skip size



    lst = [i for i in range(0,256)]

    cur_pos = 0
    skip_size = 0
    for i in range(0,64):

        for length in input_lst:
            shifted_lst = shift(lst, cur_pos)
            inverted = list(reversed(shifted_lst[:length]))
            rest = shifted_lst[length:]
            lst = shift(inverted + rest, -cur_pos)
            cur_pos = (cur_pos + (length + skip_size))%len(lst)
            skip_size +=1

    chunk_list = [lst[16*a:16*(a+1)] for a in range(0,16)]
    num_lst = [reduce((lambda x, y: x^y),chunk) for chunk in chunk_list]
    hex_lst = ["%0.2X"% num for num in num_lst]

    result = hex_lst
    return result

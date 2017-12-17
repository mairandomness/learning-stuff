
"""--- Part Two ---

The spinlock does not short-circuit. Instead, it gets more angry. At least, you assume that's what happened; it's spinning significantly faster than it was a moment ago.

You have good news and bad news.

The good news is that you have improved calculations for how to stop the spinlock. They indicate that you actually need to identify the value after 0 in the current state of the circular buffer.

The bad news is that while you were determining this, the spinlock has just finished inserting its fifty millionth value (50000000).

What is the value after 0 the moment 50000000 is inserted?"""


def main():
    skip_size = 329
    cur_position = 0
    number_list = [0]
    list_len = 0

    for i in range(1, 50000000):
        list_len +=1
        cur_position = (cur_position + skip_size) % list_len + 1
        if cur_position == 1:
            number_list.insert(cur_position, i)

    print(number_list[1])


if __name__ == "__main__":
    main()

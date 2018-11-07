import heapq


def do_math(medians, num):
    # print(num)
    max_medians = (num + medians) % 10000
    return max_medians


def _heappush_max(heap, num):

    heapq.heappush(heap, -num)


def _pushpop_max(heap, num):

    popped = heapq.heappushpop(heap, -num)

    return -popped


def peek_max_heap(heap):

    return -heap[0]


with open("Median.txt", "r") as text_file:

    data = text_file.readlines()

    # data = ['3','1','7']

    min_heap = []

    max_heap = [-int(data[0])]

    medians = int(data[0])

    for line in data[1:]:

        num = int(line)

        if ((len(min_heap) + len(max_heap)) % 2) == 0:

            if num < peek_max_heap(max_heap):

                _heappush_max(max_heap, num)

            else:

                banana = heapq.heappushpop(min_heap, num)

                _heappush_max(max_heap, banana)

        else:

            if num < peek_max_heap(max_heap):

                banana = _pushpop_max(max_heap, num)

                heapq.heappush(min_heap, banana)

            else:

                heapq.heappush(min_heap, num)

        medians = do_math(medians, peek_max_heap(max_heap))

    print(medians)

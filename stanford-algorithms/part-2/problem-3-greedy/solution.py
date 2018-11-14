# V1 V2 WEIGHT
import math


def parse_input():
    with open("input.txt", "r") as f:
        graph = {}
        for line in f.readlines()[1:]:
            v1, v2, w = [int(st) for st in line.split()]
            current_weight = graph.get((v1, v2), math.inf)
            graph[(v1, v2)] = graph[(v2, v1)] = min(w, current_weight)
    return graph


def main():
    graph = parse_input()
    first_vertex, _ = next(iter(graph))
    seen = set([first_vertex])
    total = 0

    node_num = len(set([node[0] for node in graph.keys()]))
    while len(seen) < node_num:
        curr_smallest = math.inf
        curr_key = (0, 0)
        for v1, v2 in graph.keys():
            if (v1 in seen and v2 not in seen):
                if graph[(v1, v2)] < curr_smallest:
                    curr_smallest = graph[(v1,v2)]
                    curr_key = (v1, v2)
        seen.add(curr_key[1])
        total += curr_smallest

    print(total)


if __name__ == "__main__":
    main()

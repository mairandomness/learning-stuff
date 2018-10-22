import copy
import random
import itertools

def merge_nodes (random_edge, edges):
    #deal with the edges
    edges = [edge for edge in edges if edge != random_edge]

    for edge in edges:
        if edge[0] == random_edge[1]:
            edge[0] = random_edge[0]
            edge.sort();
        if edge[1] == random_edge[1]:
            edge[1] = random_edge[0]
            edge.sort();
    return edges

def get_number_of_nodes (edges):
    return len(set(itertools.chain(*edges)))


def parse_input():
    f = open("input.txt", "r")
    text = f.read()[:-1]
    lines = text.split("\n")
    node_list = [ line.split("\t")[:-1] for line in lines ]
    edges = []
    for node in node_list :
        more_edges = [[node[0], node[i]] for i in range(1,len(node)) if node[0] < node[i]]
        edges += more_edges
    return (edges)

def main():
    initial_edges = parse_input()
    min_cut = 2000

    for i in range(0, 500):
        edges = copy.deepcopy(initial_edges)

        while get_number_of_nodes(edges) > 2:
            random_edge = random.choice(edges)
            edges = merge_nodes(random_edge, edges)

        if len(edges) < min_cut:
            min_cut = len(edges)
            print(min_cut)
            print(edges)

    print(min_cut)


if __name__ == "__main__":
    main()

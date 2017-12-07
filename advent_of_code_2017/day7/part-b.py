
"""--- Part Two ---

The programs explain the situation: they can't get down. Rather, they could get down, if they weren't expending all of their energy trying to keep the tower balanced. Apparently, one program has the wrong weight, and until it's fixed, they're stuck here.

For any program holding a disc, each program standing on that disc forms a sub-tower. Each of those sub-towers are supposed to be the same weight, or the disc itself isn't balanced. The weight of a tower is the sum of the weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo, ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc and all programs above it must each match. This means that the following sums must all be the same:

ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two. Even though the nodes above ugml are balanced, ugml itself is too heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the towers balanced. If this change were made, its weight would be 60.

Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?

"""

class tree_node:
    def __init__(self, node_lst):      #[name, weight, child_lst]
        self.name = node_lst[0]
        self.weight = node_lst[1]
        self.child_lst = node_lst[2]

        if len(self.child_lst) == 0:
            self.child_tower_weight_list=[]
        else:
            self.child_tower_weight_list = [(child.weight + sum(child.child_tower_weight_list)) for child in self.child_lst]
    # def check_tower_weight(self):
    #     result = self.weight
    #     for child in self.child_lst:
    #         if child.child_lst[0] == None:
    #             return result
    #         else:
    #             result += tree_node.check_tower_weight(child)
    #     return result


def main():
    f = open("input", "r")
    text = f.read()
    line_list = text.split("\n")[:-1]
    line_list2 = []
    for line in line_list:
        line_list2.append(line.split(" -> "))
    parent_only = []
    other_nodes = []
    for line in line_list2:
        if len(line) == 1:
            parent_only.append(line[0].split(" ") + [[]])
        else:
            other_nodes.append((line[0].split(" ") + [line[1].split(", ")]))
    all_childs = []
    for line in other_nodes:
        all_childs += line[2]
    all_nodes = parent_only + other_nodes
    for i in range(len(parent_only)):
        parent_only[i][1] = int((parent_only[i][1].replace("(", "")).replace(")", ""))
    for i in range(len(other_nodes)):
        other_nodes[i][1] = int((other_nodes[i][1].replace("(", "")).replace(")", ""))

    # for node in all_nodes:
    #     if node[0] not in all_childs:
    #         root = node
    other_nodes_copy = other_nodes[:]
    new_level_list =[1]
    new_node_level_list=[]
    tree_node_level_list=[]
    level_list = parent_only[:]
    while len(new_level_list) != 0:
        new_level_list =[]
        last_tree_node_level =[]
        for node in level_list:
            tree_node_level_list.append(tree_node(node))
            last_tree_node_level.append(tree_node(node))
            for j in range(len(other_nodes_copy)):
                try:
                    idx =other_nodes_copy[j][2].index(node[0])
                    other_nodes_copy[j][2][idx] = tree_node_level_list[-1]
                except ValueError:
                    pass
        for node in last_tree_node_level:
            if len(set(node.child_tower_weight_list))>1:
                for child in node.child_lst:
                    print(child.name, child.weight, child.weight + sum(child.child_tower_weight_list))
                new_level_list=[]
            else:
                i = len(other_nodes_copy) - 1
                while len(new_level_list) != len(level_list)/3 and i >= 0:
                    children = other_nodes_copy[i][2]
                    # any unprocessed children?
                    if any(type(child) == str for child in children):
                        i-=1
                        continue
                    new_level_list.append(other_nodes_copy[i])
                    del other_nodes_copy[i]
                    i-=1

        level_list = new_level_list[:]








if __name__ == "__main__":
    main()

graph = []
with open("dijkstraData.txt", "r") as text_file:

    data = text_file.readlines()

    for line in data:

        edges = line.split()
        result = []

        for edge in edges[1:]:

            pair = edge.split(',')
            pair = [int(i) for i in pair]
            pair[0] = pair[0] - 1

            result.append(pair)

        graph.append(result)



inf = 1000000
unseen = set([i for i in range(0, len(graph))])
score = [inf] * len(unseen)

print graph[0]

def dijkstras_path(graph, unseen, root=0):

  score[root] = 0

  currentVertex = root

  while len(unseen) > 0:

    for (vertex, weight) in graph[currentVertex]:

      if vertex in unseen:
        new_weight = score[currentVertex] + weight
        if  new_weight < score[vertex]:
          score[vertex] = new_weight

    unseen.remove(currentVertex)

    lowest = (0, inf)
    for idx, n in enumerate(score):
      if idx in unseen and n < lowest[1]:
        lowest = (idx, n)



    currentVertex = lowest[0]

  return score

ans = dijkstras_path(graph, unseen)

print ans[6]
print ans[36]
print ans[58]
print ans[81]
print ans[98]
print ans[114]
print ans[132]
print ans[164]
print ans[187]
print ans[196]
def dfs(graph, start, stack):
    stack.append(start)
    adjacency = graph[start].copy()

    for v in stack:
        if v in adjacency:
            adjacency.remove(v)
    for nxt in adjacency:
        if nxt not in stack:
            dfs(graph, nxt, stack)
    if len(stack) == len(graph.keys()):
        return stack
    elif len(stack) > 0:
        stack.pop()


def word_chain(graph):
    for key, value in graph.items():
        result = dfs(graph, key, [])
        if type(result) is list:
            return ' '.join(result)

    return "IMPOSSIBLE"


gr = {'A': ['B', 'C'],
      'B': ['A', 'D', 'E'],
      'C': ['A', 'F'],
      'D': ['B'],
      'E': ['B', 'F'],
      'F': ['C', 'E']}
print(word_chain(gr))


# dfs(graph, 'A)
# print(dfs(graph, 'A'))
# print(dfs(graph, 'B'))

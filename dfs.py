graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}


def dfs(graph, start, visited=[]):
    visited.add(start)
    print(start)
    graph[start]
    for v in visited:
        pass
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


print(dfs(graph, 'C'))

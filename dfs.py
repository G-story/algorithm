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

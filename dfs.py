def dfs(graph, word, stack, words_cnt):
    stack.append(word)

    if word[-1] in graph:
        adjacency = graph[word[-1]].copy()
    else:
        adjacency = {}

    for next_char in adjacency:
        words = adjacency[next_char]
        for word in words:
            if word not in stack:
                dfs(graph, word, stack, words_cnt)

    if len(stack) == words_cnt:
        return stack
    elif len(stack) > 0:
        stack.pop()

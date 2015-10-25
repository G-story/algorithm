from dfs import dfs


def word_chain(words):
    graph = {}

    for word in words:
        last_char = word[-1]
        next_words = list(filter(lambda x: x[0] == last_char and x != word, words))
        graph[word] = next_words

    for key, value in graph.items():
        result = dfs(graph, key, [])
        if type(result) is list:
            assert isinstance(result, list)
            return ' '.join(result)

    return "IMPOSSIBLE"

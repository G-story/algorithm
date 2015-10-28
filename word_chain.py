import string

from dfs import dfs


def word_chain(words):
    graph = {}
    first_chars = []
    last_chars = []
    for word in words:
        first_char = word[0]
        last_char = word[-1]
        first_chars.append(first_char)
        last_chars.append(last_char)
        if first_char not in graph:
            graph[first_char] = {}
        if last_char not in graph[first_char]:
            graph[first_char][last_char] = []
        graph[first_char][last_char].append(word)

    diff_char_cnt = 0
    first_char_of_chain = ''

    for char in string.ascii_lowercase:
        if first_chars.count(char) != last_chars.count(char):
            diff_char_cnt += 1
            if first_chars.count(char) > 0:
                first_char_of_chain = char

    if diff_char_cnt > 2:
        return 'IMPOSSIBLE'
    elif diff_char_cnt == 0:
        first_word = words[0]
    else:
        first_word = list(filter(lambda w: w[0] == first_char_of_chain, words))[0]

    result = dfs(graph, first_word, [], len(words))

    if type(result) is list:
        return ' '.join(result)
    else:
        return 'IMPOSSIBLE'

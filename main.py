from word_chain import word_chain


def input_output():
    word_cnt = int(input())
    words = []
    for i in range(word_cnt):
        words.append(input())
    print(word_chain(words))


def execute(func):
    n = int(input())

    for i in range(n):
        func()


execute(input_output)

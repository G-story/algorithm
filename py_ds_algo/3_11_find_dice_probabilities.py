from itertools import permutations


def find_dice_probabilities(S, n_faces=6):
    result = [x for x in permutations(range(1, n_faces + 1), 2) if sum(x) == S]
    return [len(result), result]


def test_find_dice_probabilities():
    n_faces = 6
    S = 5
    results = find_dice_probabilities(S, n_faces)
    print(results)
    assert (results[0] == len(results[1]))
    print("테스트 통과!")


if __name__ == "__main__":
    test_find_dice_probabilities()

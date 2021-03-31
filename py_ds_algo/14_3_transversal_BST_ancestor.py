from transversal_BST_recursively import BSTwithTransversalRecursively


def find_ancestor(path, low_value, high_value):
    for x in path:
        if low_value <= x <= high_value:
            return x


if __name__ == "__main__":
    bst = BSTwithTransversalRecursively()
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4, 12]
    for i in l:
        bst.add_node(i)
    print(bst)
    path = bst.preorder()
    print("전위 순회: ", path)
    print("1과 6의 공통 상위 조상 :", find_ancestor(path, 1, 6))
    print("11과 12의 공통 상위 조상: ", find_ancestor(path, 11, 12))
    print("1과 11의 공통 상위 조상: ", find_ancestor(path, 1, 11))
    print("1과 4의 공통 상위 조상: ", find_ancestor(path, 1, 4))
    print("8와 9의 공통 상위 조상: ", find_ancestor(path, 8, 9))
    print("1과 2의 공통 상위 조상: ", find_ancestor(path, 1, 2))
    print("1과 9의 공통 상위 조상: ", find_ancestor(path, 1, 9))
    print("4과 9의 공통 상위 조상: ", find_ancestor(path, 4, 9))

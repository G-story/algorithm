import heapq


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def is_child(self, node):
        max_node_x = node.value['x'] + node.value['r']
        min_node_x = node.value['x'] - node.value['r']
        max_node_y = node.value['y'] + node.value['r']
        min_node_y = node.value['y'] - node.value['r']
        max_self_x = self.value['x'] + self.value['r']
        min_self_x = self.value['x'] - self.value['r']
        max_self_y = self.value['y'] + self.value['r']
        min_self_y = self.value['y'] - self.value['r']
        if max_node_x - max_self_x <= 0 <= min_self_x - min_node_x \
                and max_node_y - max_self_y <= 0 <= min_self_y - min_node_y:
            return True
        else:
            return False

    def add_child(self, node):
        for c in self.children:
            if c.is_child(node):
                c.add_child(node)
                return
        is_added = False
        del_idxs = []
        for i, c in enumerate(self.children):
            if node.is_child(c):
                if not is_added:
                    self.children[i] = node
                    is_added = True
                else:
                    del_idxs.append(i)
                node.add_child(c)
        for i in del_idxs:
            del self.children[i]
        if not is_added:
            self.children.append(node)


class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, node):
        self.root.add_child(node)

    def get_height(self):
        sub_tree_heights = []
        for c in self.root.children:
            sub_tree = Tree(c)
            sub_tree_heights.append(sub_tree.get_height())
        if len(sub_tree_heights) > 0:
            return max(sub_tree_heights) + 1
        else:
            return 0

    def get_longest_path_distance(self):
        sub_tree_heights = []
        for c in self.root.children:
            sub_tree = Tree(c)
            sub_tree_heights.append(sub_tree.get_height())
        if len(self.root.children) == 0:
            return 0
        elif len(self.root.children) == 1:
            return self.get_height()
        else:
            return sum(heapq.nlargest(2, sub_tree_heights), 2)


def get_result():
    N = input()
    x, y, r = N * [0], N * [0], N * [0]
    inp = raw_input().split()
    x[0], y[0], r[0] = int(inp[0]), int(inp[1]), int(inp[2])
    tree = Tree(Node(dict(x=x[0], y=y[0], r=r[0])))
    for i in range(1, N):
        inp = raw_input().split()
        x[i], y[i], r[i] = int(inp[0]), int(inp[1]), int(inp[2])
        tree.insert(Node(dict(x=x[i], y=y[i], r=r[i])))
    return tree.get_longest_path_distance()


if __name__ == '__main__':
    C = input()
    for i in range(C):
        print get_result()

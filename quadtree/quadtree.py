class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []


class QuadTree:
    def __init__(self, root):
        self.root = root


def get_descendant_count(node):
    desecendant_count = 0
    for child in node.children:
        desecendant_count += 1 + get_descendant_count(child)

    return desecendant_count


def get_children(source):
    children = []
    next_i = 0

    for i, ch in enumerate(source):
        if i < next_i:
            continue
        node = Node(ch)
        children.append(node)
        if ch == 'x':
            node.children = get_children(source[i + 1:])
            next_i = i + get_descendant_count(node) + 1
        if len(children) == 4:
            break

    return children


def img_to_quadtree(compressed_img):
    quadtree = QuadTree(Node(compressed_img[0]))
    quadtree.root.children = get_children(compressed_img[1:])

    return quadtree


def quadtree_to_img(quadtree):
    img = ""
    root = quadtree.root
    img += root.data
    for child in root.children:
        if child.data == 'x':
            img += quadtree_to_img(QuadTree(child))
        else:
            img += child.data

    return img


def reverse_descendant_symmetrical(node):
    upside = node.children[:2]
    downside = node.children[2:]

    node.children = downside + upside

    for child in node.children:
        if child.data == 'x':
            reverse_descendant_symmetrical(child)


def reverse_img(compressed_img):
    quadtree = img_to_quadtree(compressed_img)
    reverse_descendant_symmetrical(quadtree.root)

    return quadtree_to_img(quadtree)


def get_img(compressed_img):
    if compressed_img[0] != 'x':
        return compressed_img
    reversed_img = reverse_img(compressed_img)

    return reversed_img


if __name__ == '__main__':
    c = int(raw_input())
    for i in xrange(c):
        compressed_img = raw_input()
        print get_img(compressed_img)

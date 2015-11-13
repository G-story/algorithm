from fortress import fortress

tree = fortress.Tree(fortress.Node(1))
tree.root.add_child(fortress.Node(2))

print tree.root.value, tree.root.left.value, tree.root.right

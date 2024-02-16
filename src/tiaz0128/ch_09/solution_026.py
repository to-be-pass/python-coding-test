class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def make_tree(self, nodes):
        length = len(nodes)

        tree = [Node(val) for val in nodes]

        for idx, node in enumerate(tree):

            if idx == 0:
                self.root = node

            left = idx * 2 + 1
            right = idx * 2 + 2

            node.left = tree[left] if left < length else None
            node.right = tree[right] if right < length else None

        return self.root

    def traversal(self, type, root):
        self.result = []

        if type == "pre":
            self.pre_order(root)
        elif type == "in":
            self.in_order(root)
        elif type == "post":
            self.post_order(root)

        return self.result

    def pre_order(self, node):
        if node:
            self.result.append(node.val)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            self.result.append(node.val)
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            self.result.append(node.val)


def solution(nodes):
    tree = BinaryTree()
    root = tree.make_tree(nodes)

    return [
        " ".join(map(str, tree.traversal("pre", root))),
        " ".join(map(str, tree.traversal("in", root))),
        " ".join(map(str, tree.traversal("post", root))),
    ]

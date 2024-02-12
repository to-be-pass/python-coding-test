class Node:
    def __init__(self, val, x, y, left=None, right=None):
        self.val = val
        self.x = x
        self.y = y

        self.left = left
        self.right = right

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None


class Tree:
    def __init__(self):
        self.arr = []

    def build_tree(self, nodeinfo):
        nodes = sorted(
            [(idx, x, y) for idx, (x, y) in enumerate(nodeinfo, 1)],
            key=lambda item: (-item[2], item[1]),
        )
        root = None

        for val, x, y in nodes:
            if root is None:
                root = Node(val, x, y)
            else:
                parent = root
                node = Node(val, x, y)

                while True:
                    if node.x < parent.x:
                        if parent.has_left():
                            parent = parent.left
                            continue
                        parent.left = node
                        break
                    else:
                        if parent.has_right():
                            parent = parent.right
                            continue
                        parent.right = node
                        break
        return root

    def traversal(self, type, root):
        self.arr = []
        if type == "pre":
            return self.pre_order(root)
        elif type == "in":
            return self.in_order(root)
        elif type == "post":
            return self.post_order(root)

    def pre_order(self, root):
        stack = [root]

        while stack:
            node = stack.pop()
            self.arr.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return self.arr

    def post_order(self, root):
        stack = [root]

        while stack:
            node = stack.pop()
            self.arr.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return self.arr[::-1]

    def in_order(self, root):
        if not root:
            return []

        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            self.arr.append(current.val)
            current = current.right

        return self.arr


def solution(nodeinfo):
    tree = Tree()
    root = tree.build_tree(nodeinfo)

    return [tree.traversal("pre", root), tree.traversal("post", root)]

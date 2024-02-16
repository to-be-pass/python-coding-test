class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def make_tree(self, lst):
        root = Node(lst[0])
        length = len(lst)

        node = root
        for val in lst[1:]:
            while True:
                if val < node.val:
                    if not node.left:
                        node.left = Node(val)
                        break
                    node = node.left
                else:
                    if not node.right:
                        node.right = Node(val)
                        break
                    node = node.right

        return root

    def search_node(self, node, search_value):
        if not node:
            return False

        if node.val == search_value:
            return True

        if node.val > search_value:
            return self.search_node(node.left, search_value)
        else:
            return self.search_node(node.right, search_value)


def solution(lst, search_lst):

    bst = BinarySearchTree()
    root = bst.make_tree(lst)

    return [bst.search_node(root, search_value) for search_value in search_lst]

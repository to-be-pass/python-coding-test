class Node:
    def __init__(self, key: int) -> None:
            self.left = None;
            self.right = None
            self.val = key

# 트리를 생성해서 돌려줍니다
def generate_tree(nodes) -> Node:
    if len(nodes) < 1 :
        return
    root = None
    if not root:
         root = Node(nodes[0])
    # 노드 삽입 시작 
    for n in nodes[1:]:
        current = root

        while True:
            if n < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(n)
                    break
            
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(n)
                    break

    return root
    
def search_value(node: Node, value: int ) -> bool:
    current = node
    while current and current.val != value:
        if value < current.val:
            current = current.left
        else:
            current = current.right

    return True if current else False



def solution(lst, search_lst):
    return [search_value(generate_tree(lst), s) for s in search_lst];



# case 1
lst = [5, 3, 8, 4, 2, 1, 7, 10]
search_lst = [1, 2, 5, 6]
print(solution(lst,search_lst))

# case 2
lst = [1, 3, 5, 7, 9]
search_lst = [2, 4, 6, 8, 10]
print(solution(lst,search_lst))




def preorder(nodes, cnt) :
    if len(nodes) > cnt:
        #print(nodes[cnt])
        result = str(nodes[cnt]) + " "
        result += preorder(nodes, (cnt * 2) + 1)
        result += preorder(nodes, (cnt * 2 ) + 2)
        return result
    else:
        return ""

def inorder(nodes, cnt) :
    if len(nodes) > cnt:
        result = inorder(nodes, (cnt * 2) + 1)
        result += str(nodes[cnt]) + " "
        result += inorder(nodes, (cnt *2) + 2)
        return result
    else:
        return "" 

def postorder(nodes, cnt) :
    if len(nodes) > cnt:
        result = postorder(nodes, (cnt * 2) + 1)
        result += postorder(nodes, (cnt * 2 ) + 2)
        result += str(nodes[cnt]) + " "
        return result
    else:
        return ""

def solution(nodes):
    # 전위, 중위, 후위 순회 결과 계산
    # 노드 리스트와 루트 노드의 인덱스를 매개변수로 각각 호출
    
    return [preorder(nodes, 0)[:-1], inorder(nodes, 0)[:-1], postorder(nodes, 0)[:-1] ]


    
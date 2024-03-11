def solution(k, operations):
    s = custom_set(k)
    for o in operations:
        if o[0] == 'u':
            s.union(o[1], o[2])
        if o[0] == 'f':
            s.find(o[1])
    return s.count()

class custom_set:
    def __init__(self, k):
        self.tree = [x for x in range(k)]
        self.rank = [0] * k

    # 경로 압축으로 최적화
    def find(self, x):
        if x == self.tree[x]:
            return x
        else:
            self.tree[x] = self.find(self.tree[x])
            return self.tree[x]

    # 랭크를 통해 최적화
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if self.rank[root_x] < self.rank[root_y]:
            self.tree[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.tree[root_y] = root_x
        else:
            self.tree[root_y] = root_x
            self.rank[root_x] += 1
    
    def count(self):
        c = 0
        for i in range(len(self.tree)):
            if i == self.tree[i]:
                c += 1
        return c
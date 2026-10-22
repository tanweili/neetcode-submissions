class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for e in edges:
            adj_list[e[0]].append(e[1])
        hs = set([i for i in range(n)])
        for ls in adj_list:
            for idx in ls:
                if idx in hs:
                    hs.remove(idx)
        if len(hs) == 1:
            return hs.pop()
        else:
            return -1
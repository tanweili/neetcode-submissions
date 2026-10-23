class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        edge_set = set()
        neighbors = {}
        for c in connections:
            edge_set.add((c[0],c[1]))
            if c[0] not in neighbors.keys():
                neighbors[c[0]] = set([c[1]])
            else:
                neighbors[c[0]].add(c[1])
            if c[1] not in neighbors.keys():
                neighbors[c[1]] = set([c[0]])
            else:
                neighbors[c[1]].add(c[0])
        q = deque()
        q.append(0)
        ans = 0
        while len(q) != 0:
            current_node = q.popleft()
            visited.add(current_node)
            for n in neighbors[current_node]:
                if n not in visited:
                    if (n, current_node) not in edge_set:
                        ans += 1
                    q.append(n)
                    visited.add(n)
        return ans
            
            
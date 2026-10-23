from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegree = [len(x) for x in graph]
        adj_list = [[] for _ in range(len(graph))]
        for i in range(len(graph)):
            for j in graph[i]:
                adj_list[j].append(i)
        q = deque()
        for i in range(len(outdegree)):
            if outdegree[i] == 0:
                q.append(i)
        ans = []
        while len(q) != 0:
            current_node = q.popleft()
            ans.append(current_node)
            for n in adj_list[current_node]:
                outdegree[n] -= 1
                if outdegree[n] == 0:
                    q.append(n)
        ans.sort()
        return ans

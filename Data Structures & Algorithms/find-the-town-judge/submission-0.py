class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0 for _ in range(n+1)]
        outdegree = [0 for _ in range(n+1)]
        for i in range(len(trust)):
            indegree[trust[i][1]] += 1
            outdegree[trust[i][0]] += 1
        for i in range(1, len(indegree)):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        return -1
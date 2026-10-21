class Solution:
    visited = set()
    adj_list = []

    def dfs(self, current_course: int) -> bool:
        if current_course in self.visited:
            return False
        if self.adj_list[current_course] == []:
            return True
        self.visited.add(current_course)
        for c in self.adj_list[current_course]:
            if self.dfs(c) == False:
                return False
        self.visited.remove(current_course)
        self.adj_list[current_course] = []
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = set()
        self.adj_list = [[] for _ in range(numCourses)]
        for p in prerequisites:
            self.adj_list[p[0]].append(p[1])
        output = True
        for i in range(numCourses):
            output = output and self.dfs(i)
        return output
        
        

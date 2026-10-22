class Solution:
    candidates = []
    target = 0
    output = []

    def backtrack(self, idx: int, current_list: List[int]) -> None:
        if sum(current_list) == self.target:
            self.output.append(current_list.copy())
            return
        elif sum(current_list) > self.target or idx >= len(self.candidates):
            return
        
        current_list.append(self.candidates[idx])
        self.backtrack(idx+1, current_list)
        current_list.pop()

        while idx + 1 < len(self.candidates) and self.candidates[idx] == self.candidates[idx+1]:
            idx += 1
        self.backtrack(idx+1, current_list)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.target = target
        self.output = []
        self.backtrack(0, [])
        return self.output
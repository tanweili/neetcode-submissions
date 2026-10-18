class Solution:
    n = 0
    ans = []
    def backtrack(self, current_string: str, open: int, close: int):
        if open > self.n or close > self.n:
            return
        if open == self.n and close == self.n:
            self.ans.append(current_string)
            return
        if close < open:
            current_string = current_string + ")"
            self.backtrack(current_string, open, close + 1)
            current_string = current_string[:-1]
        current_string = current_string + "("
        self.backtrack(current_string, open + 1, close)
        current_string = current_string[:-1]

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.ans = []
        self.backtrack("",0,0)
        return self.ans

        
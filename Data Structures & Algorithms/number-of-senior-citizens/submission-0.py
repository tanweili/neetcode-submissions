class Solution:
    def countSeniors(self, details: List[str]) -> int:
        details = map(lambda x: int(x[11:13]), details)
        ans = 0
        for n in details:
            if n > 60:
                ans += 1
        return ans
        
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            if len(ans) == 0 or ans[-1] < 0 or (ans[-1] > 0 and a > 0):
                ans.append(a)
            elif ans[-1] > 0 and ans[-1] > abs(a):
                continue
            else:
                while len(ans) > 0 and ans[-1] > 0 and ans[-1] < abs(a):
                    ans.pop()
                if len(ans) > 0 and ans[-1] > 0 and ans[-1] == abs(a):
                    ans.pop()
                    continue
                elif len(ans) > 0 and ans[-1] > 0 and ans[-1] > abs(a):
                    continue
                else:
                    ans.append(a)
        return ans

            
        
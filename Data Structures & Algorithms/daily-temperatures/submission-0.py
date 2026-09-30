class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        output = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            if len(stk) == 0 or temperatures[stk[-1]] >= temperatures[i]:
                stk.append(i)
            else:
                while len(stk) > 0 and temperatures[stk[-1]] < temperatures[i]:
                    output[stk[-1]] = i - stk[-1]
                    stk.pop()
                stk.append(i)
        return output
            
        
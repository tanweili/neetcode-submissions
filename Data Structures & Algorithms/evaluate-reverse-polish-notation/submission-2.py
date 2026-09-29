class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t not in ("+", "-", "*", "/"):
                stk.append(int(t))
            else:
                right = stk.pop()
                left = stk.pop()
                if t == "+":
                    stk.append(left + right)
                elif t == "-":
                    stk.append(left - right)
                elif t == "*":
                    stk.append(left * right)
                elif t == "/":
                    stk.append(int(left / right))
        return stk[-1]

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i in ("(","{","["):
                stk.append(i)
            elif i == ")":
                if len(stk) > 0 and stk[-1] == "(":
                    stk.pop()
                else:
                    return False
            elif i == "}":
                if len(stk) > 0 and stk[-1] == "{":
                    stk.pop()
                else:
                    return False
            elif i == "]":
                if len(stk) > 0 and stk[-1] == "[":
                    stk.pop()
                else:
                    return False
        return len(stk) == 0
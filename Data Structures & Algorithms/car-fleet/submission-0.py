class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        for i in range(len(position)):
            stk.append((position[i],speed[i]))
        stk.sort(key=lambda x: x[0])
        # print(stk)
        stk = [(target - x[0]) / x[1] for x in stk]
        # print(stk)
        fleet_time = None
        output = 0
        while len(stk) > 0:
            if fleet_time == None or stk[-1] > fleet_time:
                output += 1
                fleet_time = stk.pop()
            else:
                stk.pop()
        return output




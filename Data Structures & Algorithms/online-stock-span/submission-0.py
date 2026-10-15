class StockSpanner:
    def __init__(self):
        self.stk = []
        
    def next(self, price: int) -> int:
        if len(self.stk) == 0 or self.stk[-1][0] > price:
            self.stk.append((price, 1))
            return 1
        else:
            current_cnt = 1
            while len(self.stk) > 0 and self.stk[-1][0] <= price:
                _, cnt = self.stk.pop()
                current_cnt += cnt
            self.stk.append((price, current_cnt))
            return current_cnt

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
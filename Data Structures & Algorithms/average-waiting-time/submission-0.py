class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_waiting_time = 0
        for i in range(len(customers)):
            time_finished = max(customers[i][0] + customers[i][1], current_time + customers[i][1])
            total_waiting_time += time_finished - customers[i][0]
            current_time = time_finished
        return total_waiting_time / len(customers)
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0
        for i in range(len(customers)):
            total_waiting_time += customers[i][1]
            if i == 0:
                running_time = sum(customers[i])
                continue
            if running_time > customers[i][0]:
                total_waiting_time += running_time - customers[i][0]
                running_time += customers[i][1]
            else:
                running_time = sum(customers[i])
        return total_waiting_time / len(customers)

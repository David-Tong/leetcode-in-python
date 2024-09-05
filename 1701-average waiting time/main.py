class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        # pre-process
        L = len(customers)
        total = 0

        # process
        curr = 0
        for customer in customers:
            arrival, time = customer
            curr = max(curr, arrival) + time
            wait = curr - arrival
            total += wait

        return total * 1.0 / L


customers = [[1,2],[2,5],[4,3]]
customers = [[5,2],[5,4],[10,3],[20,1]]

solution = Solution()
print(solution.averageWaitingTime(customers))

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum_gas = 0
        sum_cost = 0
        for x in range(len(gas)):
            sum_gas += gas[x]
            sum_cost += cost[x]

        if sum_gas < sum_cost:
            return -1

        sum = 0
        start = 0
        for x in range(len(gas)):
            sum += gas[x]
            sum -= cost[x]
            if sum < 0:
                start = x + 1
                sum = 0

        if start >= len(gas):
            return -1
        else:
            return start


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

gas = [2, 3, 4]
cost = [3, 4, 3]

gas = [5, 1, 2, 3, 4]
cost = [4, 4, 1, 5, 1]

solution = Solution()
print(solution.canCompleteCircuit(gas, cost))

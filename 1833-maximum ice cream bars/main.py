class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        for cost in costs:
            heappush(heap, cost)

        ans = 0
        while heap and  coins >= heap[0]:
            cost = heappop(heap)
            coins -= cost
            ans += 1
        return ans


costs = [1,3,2,4,1]
coins = 7

costs = [10,6,8,7,7,8]
coins = 5

costs = [1,6,3,1,2,5]
coins = 20

costs = [20]
coins = 10

solution = Solution()
print(solution.maxIceCream(costs, coins))

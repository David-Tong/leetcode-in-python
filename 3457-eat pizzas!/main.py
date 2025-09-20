class Solution(object):
    def maxWeight(self, pizzas):
        """
        :type pizzas: List[int]
        :rtype: int
        """
        # pre-process
        L = len(pizzas)
        days = L // 4
        odds = (days + 1) // 2
        evens = days // 2

        # process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        for pizza in pizzas:
            heappush(heap, -1 * pizza)

        ans = 0
        # odd days
        for _ in range(odds):
            ans -= heappop(heap)

        # even days
        for _ in range(evens):
            heappop(heap)
            ans -= heappop(heap)
        return ans


pizzas = [1,2,3,4,5,6,7,8]
pizzas = [2,1,1,1,1,1,1,1]
pizzas = [6,5,6,10,5,6,7,6,5,8,10,5]

from random import randint
pizzas = [randint(1, 10 ** 5) for _ in range(2 * 10 ** 4)]
print(pizzas)

solution = Solution()
print(solution.maxWeight(pizzas))

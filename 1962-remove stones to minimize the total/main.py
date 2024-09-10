class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for pipe in piles:
            heappush(heap, pipe * -1)

        from math import floor
        for x in range(k):
            pile = heappop(heap)
            pile = floor(pile / 2.0)
            heappush(heap, pile)

        ans = int(sum(heap) * -1)
        return ans


piles = [5,4,9]
k = 2

piles = [4,3,6,7]
k = 3

piles = [1]
k = 100

solution = Solution()
print(solution.minStoneSum(piles, k))

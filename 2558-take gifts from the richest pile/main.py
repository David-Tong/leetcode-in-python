from numpy.ma import floor


class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        for gift in gifts:
            heappush(heap, -1 * gift)

        # process
        from math import sqrt
        for x in range(k):
            item = -1 * heappop(heap)
            heappush(heap, -1 * int(sqrt(item)))

        ans = -1 * sum(heap)
        return ans


gifts = [25,64,9,4,100]
k = 4

gifts = [1,1,1,1]
k = 4

gifts = [25,64,9,4,100]
k = 1000

solution = Solution()
print(solution.pickGifts(gifts, k))

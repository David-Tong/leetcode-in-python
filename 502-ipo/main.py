class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        L = len(profits)

        pairs = zip(profits, capital)
        pairs = sorted(pairs, key=lambda x: x[1])

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        count = 0
        index = 0
        while count < k:
            # put all possible profits
            while index < L and pairs[index][1] <= w:
                heappush(heap, pairs[index][0] * -1)
                index += 1
            # fetch the highest profit
            if heap:
                w -= heappop(heap)
                count += 1
            else:
                break
        return w


k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]

k = 3
w = 0
profits = [1,2,3]
capital = [0,1,2]

k = 3
w = 0
profits = [5,10,3]
capital = [1,1,1]

k = 3
w = 0
profits = [5, 25, 15]
capital = [0, 10, 15]

solution = Solution()
print(solution.findMaximizedCapital(k, w, profits, capital))

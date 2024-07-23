class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        # pre-process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        heappush(heap, -1 * a)
        heappush(heap, -1 * b)
        heappush(heap, -1 * c)

        # process
        ans = 0
        while len(heap) > 1:
            item = heappop(heap)
            item2 = heappop(heap)
            item, item2 = item + 1, item2 + 1
            if item < 0:
                heappush(heap, item)
            if item2 < 0:
                heappush(heap, item2)
            ans += 1
        return ans


a = 2
b = 4
c = 6

a = 1
b = 8
c = 8

a = 13092
b = 34211
c = 6002

solution = Solution()
print(solution.maximumScore(a, b, c))

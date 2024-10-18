class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        for num in nums:
            heappush(heap, num * -1)

        # process
        from math import ceil
        ans = 0
        for _ in range(k):
            num = int(heappop(heap) * -1)
            ans += num
            heappush(heap, ceil(num * 1.0 / 3) * -1)
        return ans


nums = [10,10,10,10,10]
k = 5

nums = [1,10,3,3,3]
k = 3

nums = [1]
k = 3

solution = Solution()
print(solution.maxKelements(nums, k))

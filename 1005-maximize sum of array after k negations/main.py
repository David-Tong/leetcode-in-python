class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # process
        from heapq import heapify, heappush, heappop
        heap = list(nums)
        heapify(heap)

        index = 0
        while index < k:
            num = heappop(heap)
            heappush(heap, num * -1)
            index += 1

        # post-process
        ans = sum(heap)
        return ans


nums = [4,2,3]
k = 1

nums = [3,-1,0,2]
k = 3

nums = [2,-3,-1,5,-4]
k = 2

solution = Solution()
print(solution.largestSumAfterKNegations(nums, k))

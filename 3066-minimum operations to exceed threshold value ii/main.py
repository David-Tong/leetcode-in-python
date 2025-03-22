class Solution(object):
    def minOperations(self, nums, k):
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
            heappush(heap, num)

        # process
        num = heap[0]
        ans = 0
        while num < k:
            num, num2 = heappop(heap), heappop(heap)
            heappush(heap, min(num, num2) * 2 + max(num, num2))
            ans += 1
            num = heap[0]
        return ans


nums = [2,11,10,1,3]
k = 10

nums = [1,1,2,4,9]
k = 20

nums = [1,1]
k = 2

solution = Solution()
print(solution.minOperations(nums, k))

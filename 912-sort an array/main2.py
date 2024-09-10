class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for num in nums:
            heappush(heap, num)

        ans = list()
        while heap:
            ans.append(heappop(heap))
        return ans


nums = [1,3,7,8,2,4,5,6,9,10]
nums = [3] + [2] * 100000

solution = Solution()
print(solution.sortArray(nums))
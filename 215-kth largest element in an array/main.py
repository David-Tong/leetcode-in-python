from queue import PriorityQueue as PQ


class Solution:
    def findKthLargest(self, nums, k):
        pq = PQ()
        for num in nums:
            pq.put(num)
            if pq.qsize() > k:
                pq.get()
        return pq.get()


nums = [3, 2, 1, 5, 6, 4]
k = 2

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

sol = Solution()
print(sol.findKthLargest(nums, k))
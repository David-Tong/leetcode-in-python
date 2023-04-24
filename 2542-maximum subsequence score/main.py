class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        pairs = zip(nums1, nums2)
        pairs = sorted(pairs, key=lambda x: -x[1])

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        total = 0
        ans = float("-inf")
        for pair in pairs:
            heappush(heap, pair[0])
            total += pair[0]
            if len(heap) > k:
                item = heappop(heap)
                total -= item
            if len(heap) == k:
                ans = max(ans, total * pair[1])
        return ans


nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3

"""
nums1 = [4,2,3,1,1]
nums2 = [7,5,10,9,6]
k = 1

nums1 = [1]
nums2 = [2]
k = 1
"""

solution = Solution()
print(solution.maxScore(nums1, nums2, k))

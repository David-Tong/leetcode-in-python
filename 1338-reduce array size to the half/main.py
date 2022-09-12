class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import defaultdict
        dicts = defaultdict(int)
        for item in arr:
            dicts[item] += 1

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        for item in dicts:
            heappush(heap, dicts[item] * -1)

        target = len(arr) // 2
        l = 0
        ans = 0
        while l < target:
            l -= heappop(heap)
            ans += 1

        return ans


arr = [3,3,3,3,5,5,5,2,2,7]
arr = [7,7,7,7,7,7]
arr = [1,1,1,1,2,2,2]
arr = [1,1,1,1,2,2,2,2]
arr = []

solution = Solution()
print(solution.minSetSize(arr))

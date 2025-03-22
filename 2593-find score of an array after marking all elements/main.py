from imageop import scale


class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        marked = set()
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for idx, num in enumerate(nums):
            heappush(heap, (num, idx))

        # process
        ans = 0
        while len(marked) < L:
            num, idx = heappop(heap)
            if idx not in marked:
                marked.add(idx)
                if idx - 1 >= 0:
                    marked.add(idx - 1)
                if idx + 1 < L:
                    marked.add(idx + 1)
                ans += num
        return ans


nums = [2,1,3,4,5,2]
nums = [2,3,5,1,3,2]
nums = [1]
nums = [1,1,1,1,1,1]

solution = Solution()
print(solution.findScore(nums))

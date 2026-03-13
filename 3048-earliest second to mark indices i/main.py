class Solution(object):
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        """
        :type nums: List[int]
        :type changeIndices: List[int]
        :rtype: int
        """
        # pre-process
        M = len(nums)
        N = len(changeIndices)

        def can(target):
            from collections import defaultdict
            dicts = defaultdict(int)
            for idx in range(target):
                dicts[changeIndices[idx]] = idx + 1
            if len(dicts) < M:
                return False

            from heapq import heapify, heappush, heappop
            heap = list()
            heapify(heap)
            for k, v in dicts.items():
                heappush(heap, (v, k - 1))

            cost = 0
            while heap:
                timing, idx = heappop(heap)
                cost += nums[idx] + 1
                if cost > timing:
                    return False
            return True

        # process
        left, right = 1, N
        while left + 1 < right:
            middle = (left + right) // 2
            if can(middle):
                right = middle
            else:
                left = middle + 1
        if can(left):
            return left
        elif can(right):
            return right
        else:
            return -1


nums = [2,2,0]
changeIndices = [2,2,2,2,3,2,2,1]

nums = [1,3]
changeIndices = [1,1,1,2,1,1,1]

nums = [0,1]
changeIndices = [2,2,2]

solution = Solution()
print(solution.earliestSecondToMarkIndices(nums, changeIndices))

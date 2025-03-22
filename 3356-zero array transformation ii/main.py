class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        # short-cut
        zero = True
        for x in range(L):
            if nums[x] > 0:
                zero = False
                break
        if zero:
            return 0

            # process
        # helper function
        def canTransform(n):
            # calculate diffs
            diffs = [0] * L
            for x in range(n):
                up, down, delta = queries[x]
                diffs[up] -= delta
                if down < L - 1:
                    diffs[down + 1] += delta
            # apply diff
            diff = 0
            for x in range(L):
                diff += diffs[x]
                if nums[x] + diff > 0:
                    return False
            return True

        # binary search
        left, right = 1, len(queries)
        while left + 1 < right:
            middle = (left + right) // 2
            if canTransform(middle):
                right = middle
            else:
                left = middle + 1

        if canTransform(left):
            return left
        elif canTransform(right):
            return right
        else:
            return -1


nums = [2,0,2]
queries = [[0,2,1],[0,2,1],[1,1,3]]

nums = [4,3,2,1]
queries = [[1,3,2], [0,2,1]]

nums = [5]
queries = [[0,0,5],[0,0,1],[0,0,3],[0,0,2]]


solution = Solution()
print(solution.minZeroArray(nums, queries))

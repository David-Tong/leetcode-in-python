class Solution(object):
    def canMakeEqual(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # pre-process
        L = len(nums)

        idx, idx2 = -1, -1
        positives, negatives = 0, 0
        for x in range(L):
            if nums[x] == 1:
                if idx == -1:
                    idx = x
                else:
                    positives += x - idx
                    idx = -1
            elif nums[x] == -1:
                if idx2 == -1:
                    idx2 = x
                else:
                    negatives += x - idx2
                    idx2 = -1

        counts = float("inf")
        if idx == -1:
            counts = min(counts, positives)
        if idx2 == -1:
            counts = min(counts, negatives)

        return True if counts <= k else False


nums = [1,-1,1,-1,1]
k = 3

nums = [-1,-1,-1,1,1,1]
k = 5

nums = [1,-1,1]
k = 2

solution = Solution()
print(solution.canMakeEqual(nums, k))

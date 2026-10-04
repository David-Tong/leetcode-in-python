class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        maxi = float('-inf')
        maxis = list()
        idx = 0
        while idx < L:
            maxi = max(maxi, nums[idx])
            maxis.append(maxi)
            idx += 1

        mini = float('inf')
        minis = list()
        idx = L - 1
        while idx >= 0:
            mini = min(mini, nums[idx])
            minis.append(mini)
            idx -= 1
        minis.reverse()

        # process
        idx = 0
        while idx < L:
            stability = maxis[idx] - minis[idx]
            if stability <= k:
                return idx
            idx += 1
        return -1


nums = [5,0,1,4]
k = 3

nums = [3,2,1]
k = 1

nums = [0]
k = 0

solution = Solution()
print(solution.firstStableIndex(nums, k))
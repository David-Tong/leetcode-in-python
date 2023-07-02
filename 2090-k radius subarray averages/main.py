class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(nums)
        ans = [-1] * N

        if 2 * k + 1 <= N:
            total = sum(nums[0: 2 * k + 1])
        else:
            return ans

        idx = k
        while idx + k < N:
            ans[idx] = total / (2 * k + 1)
            total -= nums[idx - k]
            if idx + k + 1 < N:
                total += nums[idx + k + 1]
            idx += 1
        return ans


nums = [7,4,3,9,1,8,5,2,6]
k = 3

nums = [100000]
k = 0

nums = [8]
k = 100000

nums = [2,3,4,5,6,8,11,1,4]
k = 1

solution = Solution()
print(solution.getAverages(nums, k))

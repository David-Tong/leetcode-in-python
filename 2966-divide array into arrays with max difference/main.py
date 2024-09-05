class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        ans = list()
        for x in range(0, L, 3):
            if nums[x + 2] - nums[x] <= k:
                ans.append(nums[x: x+ 3])
            else:
                return list()
        return ans


nums = [1,3,4,8,7,9,3,5,1]
k = 2

nums = [1,3,3,2,7,3]
k = 3

nums = [1,4,5,3,1,2,31,2,3,2,1,4,1,7,8]
k = 2

solution = Solution()
print(solution.divideArray(nums, k))

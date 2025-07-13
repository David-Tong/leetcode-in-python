class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # conner case
        if L == 1:
            if k % 2 == 1:
                return -1

        # process
        if k > L:
            ans = max(nums)
        elif k == L:
            ans = max(nums[:k - 1])
        else:
            if k > 1:
                ans = max(max(nums[:k - 1]), nums[k])
            else:
                ans = nums[k]
        return ans


nums = [5,2,2,4,0,6]
k = 4

nums = [2]
k = 1

nums = [2,3,4,5,7,9]
k = 4

nums = [2,3,4,5,3,9]
k = 4

nums = [99,95,68,24,18]
k = 69

nums = [68,76,53,73,85,87,58,24,48,59,38,80,38,65,90,38,45,22,3,28,11]
k = 1

nums = [18]
k = 3

nums = [0,1,2]
k = 3

solution = Solution()
print(solution.maximumTop(nums, k))

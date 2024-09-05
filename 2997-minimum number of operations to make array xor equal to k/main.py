class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        xor = nums[0]
        for x in range(1, L):
            xor ^= nums[x]
        xor ^= k

        # process
        ans = 0
        while xor:
            ans += xor & 1
            xor >>= 1
        return ans


nums = [2,1,3,4]
k = 1

nums = [2,0,2,0]
k = 0

nums = [104,5,6,11,2,3,8]
k = 3

solution = Solution()
print(solution.minOperations(nums, k))

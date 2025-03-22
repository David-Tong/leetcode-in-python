class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def countSetBits(num):
            L = 9
            bits = 0
            for x in range(L):
                if num >> x & 1:
                    bits += 1
            return bits

        # pre-process
        N = len(nums)
        bits = list()
        for num in nums:
            bits.append(countSetBits(num))
        # print(bits)

        # process
        # bubble sort
        for x in range(N):
            for y in range(N - 1):
                if nums[y] > nums[y + 1] and bits[y] == bits[y + 1]:
                    nums[y], nums[y + 1] = nums[y + 1], nums[y]
        # print(nums)

        for x in range(1, N):
            if nums[x] < nums[x - 1]:
                return False
        return True


nums = [8,4,2,30,15]
"""
nums = [1,2,3,4,5]
nums = [3,16,8,4,2]
nums = [5,4,3,2,1]
nums = [1,1,3,4,5]
nums = [75,34,30]
"""

solution = Solution()
print(solution.canSortArray(nums))

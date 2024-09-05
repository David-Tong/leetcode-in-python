class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        L = len(nums)
        nums = sorted(nums)

        def canPair(target):
            pairs = 0
            idx = 0
            while idx < L - 1:
                if nums[idx + 1] - nums[idx] <= target:
                    pairs += 1
                    idx += 2
                else:
                    idx += 1

            if pairs >= p:
                return True
            else:
                return False

        left = 0
        right = 10 ** 9

        while left + 1 < right:
            middle = (left + right) // 2
            if canPair(middle):
                right = middle
            else:
                left = middle + 1

        if canPair(left):
            return left
        else:
            return right


nums = [10,1,2,7,1,3]
p = 2

nums = [4,2,1,2]
p = 1

nums = [9,3,4,5,6,11,2,3,4,5,11,34,7,12,9]
p = 4

solution = Solution()
print(solution.minimizeMax(nums, p))

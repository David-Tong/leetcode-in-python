class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        count = 1
        increasings = list()
        for x in range(1, L):
            if nums[x] > nums[x - 1]:
                count += 1
            else:
                increasings.append(count)
                count = 1
        increasings.append(count)
        # print(increasings)
        I = len(increasings)

        # process
        def can(k):
            idx = 0
            while idx < I:
                if idx > 0:
                    if increasings[idx] >= k and increasings[idx - 1] >= k:
                        return True
                if increasings[idx] >= 2 * k:
                    return True
                idx += 1
            return False

        # binary search
        left = 1
        right = L // 2
        while left + 1 < right:
            middle = (left + right) // 2
            if can(middle):
                left = middle
            else:
                right = middle - 1

        if can(right):
            return right
        else:
            return left


nums = [2,5,7,8,9,2,3,4,3,1]
nums = [1,2,3,4,4,4,4,5,6,7]

solution = Solution()
print(solution.maxIncreasingSubarrays(nums))

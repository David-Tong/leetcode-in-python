class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # short cuts
        if L == 2:
            return abs(nums[0] - nums[1])

        # find the first position where strictly increasing subarray ends
        pos = -1
        equal_pos = -1
        presums = list()
        presums.append(0)
        idx = 0
        while idx < L - 1:
            if nums[idx] > nums[idx + 1]:
                if pos == -1:
                    pos = idx
            elif nums[idx] == nums[idx + 1]:
                if equal_pos == -1:
                    equal_pos = idx
                else:
                    return -1
            else:
                if pos != -1:
                    return -1
            presums.append(presums[-1] + nums[idx])
            idx += 1
        presums.append(presums[-1] + nums[idx])

        if equal_pos != -1:
            idx = equal_pos
            while idx > 0:
                if nums[idx] <= nums[idx - 1]:
                    return -1
                idx -= 1
            idx = equal_pos + 1
            while idx < L - 1:
                if nums[idx] <= nums[idx + 1]:
                    return - 1
                idx += 1
            return abs(presums[L] - presums[equal_pos + 1] * 2)

        # it is a strictly increasing array
        if pos == -1:
            pos = L - 1

        print(pos)

        # process
        if pos == 0:
            ans = abs(presums[L] - presums[1] * 2)
        elif pos == L - 1:
            ans = abs(presums[L] - presums[L - 1] * 2)
        else:
            ans = min(abs(presums[L] - presums[pos + 1] * 2), abs(presums[L] - presums[pos] * 2))
        return ans


nums = [1,2,3,4]
"""
nums = [4,3,2,1]
nums = [1,2,4,3]
nums = [1,3,2,4]
"""

nums = [3,2,2]
nums = [1,3,5,5,4,2]

"""
from random import randint
nums = [randint(1,10 ** 5) for _ in range(10 ** 5)]
print(nums)
"""

solution = Solution()
print(solution.splitArray(nums))

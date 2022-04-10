from collections import defaultdict


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicts = defaultdict(int)
        dicts[0] = -1

        sum = 0
        index = 0
        ans = 0
        for num in nums:
            if num == 1:
                sum += 1
            elif num == 0:
                sum -= 1
            if sum not in dicts.keys():
                dicts[sum] = index
            else:
                ans = max(ans, index - dicts[sum])
            index += 1
        return ans


nums = [0, 1]
nums = [0, 1, 0]
nums = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
nums = [0]
solution = Solution()
print(solution.findMaxLength(nums))
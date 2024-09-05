class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        for num in nums:
            dicts[num] += 1

        # process
        ans = list()
        for num in nums:
            if dicts[num] > 1:
                pass
            else:
                if dicts[num - 1] > 0 or dicts[num + 1] > 0:
                    pass
                else:
                    ans.append(num)
        return ans


nums = [10,6,5,8]
nums = [1,3,5,3]

solution = Solution()
print(solution.findLonely(nums))

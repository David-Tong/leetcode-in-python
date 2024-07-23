class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        for num in nums:
            dicts[num] += 1

        L = max(dicts.values())

        # process
        ans = [list() for _ in range(L)]

        for key in dicts:
            for x in range(dicts[key]):
                ans[x].append(key)

        return ans


nums = [1,3,4,1,2,3,1]
nums = [1,2,3,4]
nums = [1,1,1,1,2,3,4,2,1,2,3,1,2,6]

solution = Solution()
print(solution.findMatrix(nums))

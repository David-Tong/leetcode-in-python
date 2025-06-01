class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        from collections import defaultdict
        dicts = defaultdict(int)
        start = 0
        for x in range(L - 1, -1, -1):
            dicts[nums[x]] += 1
            if dicts[nums[x]] > 1:
                start = x + 1
                break

        # print(start)

        # process
        if start % 3 == 0:
            ans = start // 3
        else:
            ans = start // 3 + 1
        return ans

nums = [1,2,3,4,2,3,3,5,7]
nums = [1,1,2,3,4,5,6,7]
nums = [4,5,6,4,4]
nums = [6,7,8,9]

solution = Solution()
print(solution.minimumOperations(nums))

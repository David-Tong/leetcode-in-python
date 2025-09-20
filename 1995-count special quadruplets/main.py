class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, num in enumerate(nums):
            dicts[num].append(idx)

        # process
        ans = 0
        for x in range(L):
            for y in range(x + 1, L):
                for z in range(y + 1, L):
                    target = nums[x] + nums[y] + nums[z]
                    if target in dicts:
                        for t in range(len(dicts[target]) - 1, -1, -1):
                            if dicts[target][t] > z:
                                ans += 1
        return ans


nums = [1,2,3,6]
nums = [3,3,6,4,5]
nums = [1,1,1,3,5]
nums = [1,1,1,3,5,5]

solution = Solution()
print(solution.countQuadruplets(nums))

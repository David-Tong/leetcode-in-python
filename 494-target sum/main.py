class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = len(nums)

        def doFind(idx, total):
            key = str(idx) + "-" + str(total)
            if key in self.cache:
                return self.cache[key]

            if idx == L:
                if total == target:
                    return 1
                else:
                    return 0

            ans = doFind(idx + 1, total - nums[idx]) + doFind(idx + 1, total + nums[idx])
            self.cache[key] = ans
            return ans

        from collections import defaultdict
        self.cache = defaultdict(int)

        return doFind(0, 0)


nums = [1,1,1,1,1]
target = 3

nums = [1]
target = 1

nums = [1,2,3,4,5,5,6,1,3]
target = 12

nums = [48,9,50,48,38,34,47,8,1,44,27,42,45,25,23,40,6,39,21,48]
target = 29

solution = Solution()
print(solution.findTargetSumWays(nums, target))

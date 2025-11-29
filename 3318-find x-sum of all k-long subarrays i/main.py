class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)

        # helper function
        def xsum(nums):
            from collections import defaultdict
            dicts = defaultdict(int)
            for num in nums:
                dicts[num] += 1

            frequency = list()
            for num in dicts:
                frequency.append((dicts[num], num))
            frequency = sorted(frequency, reverse=True)

            res = 0
            idx = 0
            while idx < x and idx < len(frequency):
                res += frequency[idx][0] * frequency[idx][1]
                idx += 1
            return res

        # process
        ans = list()
        for idx in range(L - k + 1):
            ans.append(xsum(nums[idx:idx + k]))
        return ans


nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2

nums = [3,8,7,8,7,5]
k = 2
x = 2

nums = [1,1,1,1,1,1,1,1,1,1,1]
k = 6
x = 2

solution = Solution()
print(solution.findXSum(nums, k, x))
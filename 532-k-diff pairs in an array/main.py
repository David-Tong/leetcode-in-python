from collections import defaultdict

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dct = defaultdict(int)
        for num in nums:
            dct[num] += 1

        ans = 0
        for key in sorted(dct.keys()):
            if k == 0:
               if dct[key] > 1:
                   ans += 1
            else:
                if key + k in dct.keys():
                    ans += 1
        return ans


nums = [3, 1, 4, 1, 5]
k = 2

nums = [1, 2, 3, 4, 5]
k = 1

nums = [1,3,1,5,4]
k = 0

solution = Solution()
print(solution.findPairs(nums, k))

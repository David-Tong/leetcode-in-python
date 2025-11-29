class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)

        from collections import defaultdict
        dicts = defaultdict(int)
        from sortedcontainers import SortedList
        keys = SortedList()

        # helper function
        def getBeauty():
            total = 0
            for key in keys:
                if key >= 0:
                    return 0
                total += dicts[key]
                if total >= x:
                    return key

        # process
        for idx in range(k):
            dicts[nums[idx]] += 1
        for key in dicts:
            keys.add(key)

        ans = list()
        ans.append(getBeauty())
        for idx in range(k, L):
            dicts[nums[idx - k]] -= 1
            if dicts[nums[idx - k]] == 0:
                keys.remove(nums[idx - k])
            dicts[nums[idx]] += 1
            if nums[idx] not in keys:
                keys.add(nums[idx])
            ans.append(getBeauty())
        return ans


nums = [1,-1,-3,-2,3]
k = 3
x = 2

nums = [-1,-2,-3,-4,-5]
k = 2
x = 2

nums = [-3,1,2,-3,0,-3]
k = 2
x = 1

from random import randint
nums = [randint(-50, 50) for _ in range(10 ** 5)]
print(nums)
k = 1000
x = 500

solution = Solution()
# print(solution.getSubarrayBeauty(nums, k, x))

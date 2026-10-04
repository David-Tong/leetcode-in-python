class Solution(object):
    def mostFrequentIDs(self, nums, freq):
        """
        :type nums: List[int]
        :type freq: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)

        # process
        from collections import defaultdict
        dicts = defaultdict(int)

        from sortedcontainers import SortedList
        sl = SortedList()

        ans = list()
        idx = 0
        while idx < L:
            prev = dicts[nums[idx]]
            if prev > 0:
                sl.remove(prev)
            dicts[nums[idx]] += freq[idx]
            sl.add(dicts[nums[idx]])
            ans.append(sl[-1])
            idx += 1
        return ans


nums = [2,3,2,1]
freq = [3,2,-3,1]

nums = [5,5,3]
freq = [2,-2,1]

from random import randint
nums = [randint(1 , 10 ** 5) for _ in range(10 ** 3)]
freq = [randint(0, 10 ** 5) for _ in range(10 ** 3)]

print(nums)
print(freq)

solution = Solution()
print(solution.mostFrequentIDs(nums, freq))

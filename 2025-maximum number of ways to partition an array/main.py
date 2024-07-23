class Solution(object):
    def waysToPartition(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        L = len(nums)

        # pre-process
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, num in enumerate(nums):
            dicts[k - num].append(idx)
        print(dicts)

        # presum
        presums = [0]
        for num in nums:
            presums.append(presums[-1] + num)
        total = presums[-1]

        # enumerate
        diffs = defaultdict(list)
        for x in range(1, L):
            diff = presums[x] - (total - presums[x])
            diffs[diff].append(x)
        print(diffs)

        # process
        ans = 0
        # conner case
        if 0 in diffs:
            ans = len(diffs[0])

        # enumerate
        from bisect import bisect_left, bisect_right
        for key in dicts:
            for item in dicts[key]:
                ways = 0
                # search left
                if -1 * key in diffs:
                    idx = bisect_right(diffs[-1 * key], item)
                    ways += len(diffs[-1 * key]) - idx
                # search right
                if key in diffs:
                    idx = bisect_right(diffs[key], item)
                    ways += idx
                ans = max(ans, ways)
        return ans


nums = [2,-1,2]
k = 3

nums = [0,0,0]
k = 1

nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14]
k = -33

nums = [2,2,0,0,2,0,2,0,2,0,2,0,2,0,2,2,2]
k = 2

nums = [0,0,0,0,0,0,0,0,0,-4732,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
k = -4732

nums = [0,0,0,-4732,0,0,0,0]
k = -4732

"""
nums = [0,0,-1,1,-1,1,-4732,0,0,0,-1,1,-1,1,0,0,0]
k = -4732

nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30827,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
k = 0

nums = [0,0,30827,0]
k = 0

nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-71,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-5,0]
k = 76

nums = [0,0,0,-71,0,0,-5,0]
k = 76
"""

solution = Solution()
print(solution.waysToPartition(nums, k))
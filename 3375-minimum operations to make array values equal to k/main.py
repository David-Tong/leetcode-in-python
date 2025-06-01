class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        unique = set()
        for num in nums:
            unique.add(num)
        unique = sorted(unique)
        L = len(unique)

        # short-cut
        if L == 1 and k == unique[-1]:
            return 0
        else:
            if k > unique[0]:
                return -1

        # process
        from bisect import bisect_right
        idx = bisect_right(unique, k)
        ans = len(unique) - idx
        return ans


nums = [5,2,5,4,5]
k = 2

nums = [2,1,2]
k = 2

nums = [9,7,5,3]
k = 1

nums = [1]
k = 1

nums = [6,9,2,2]
k = 5

solution = Solution()
print(solution.minOperations(nums, k))

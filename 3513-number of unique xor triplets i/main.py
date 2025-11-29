class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        N = max(nums)
        powers = [2 ** x for x in range(20)]
        # print(powers)

        # process
        if N < 3:
            return N
        elif N == 3:
            return 4
        else:
            from bisect import bisect_right
            idx = bisect_right(powers, N)
            # print(idx)
            return 2 ** idx


solution = Solution()
nums = [1,2]
nums = [3,1,2]
nums = [1,2,3,4,5]
nums = [1,2,3,4,5,6,7,8,9,10]
nums = [_ for _ in range(115)]
nums = [_ for _ in range(256)]

nums = [_ for _ in range(10 ** 5)]
print(nums)

print(solution.uniqueXorTriplets(nums))

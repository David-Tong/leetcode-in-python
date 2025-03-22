class Solution(object):
    def minOperations(self, nums, numsDivide):
        """
        :type nums: List[int]
        :type numsDivide: List[int]
        :rtype: int
        """
        # pre-process
        # helper function : gcd
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        L = len(numsDivide)
        cd = numsDivide[0]
        for x in range(L):
            cd = gcd(cd, numsDivide[x])

        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1

        # process
        deletions = 0
        for num in sorted(dicts.keys()):
            if cd % num == 0:
                return deletions
            else:
                deletions += dicts[num]
        return -1


nums = [2,3,2,4,3]
numsDivide = [9,6,9,3,15]

nums = [4,3,6]
numsDivide = [8,2,6,10]

solution = Solution()
print(solution.minOperations(nums, numsDivide))

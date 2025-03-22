class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(candies)

        # process
        # greedy function
        def canAllocate(target):
            if target == 0:
                return True
            count = 0
            for x in range(L):
                count += candies[x] // target
            if count >= k:
                return True
            else:
                return False

        # binary search
        left, right = 0, max(candies)
        while left + 1 < right:
            middle = (left + right) // 2
            if canAllocate(middle):
                left = middle
            else:
                right = middle - 1

        if canAllocate(right):
            return right
        else:
            return left


candies = [5,8,6]
k = 3

candies = [2,5]
k = 11

candies = [4,7,5]
k = 17

candies = [3102006,6279432,7216621,3628028,5711306,2292506,2107393]
k = 23626985

solution = Solution()
print(solution.maximumCandies(candies, k))

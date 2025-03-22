class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        # pre-process
        banned = set(banned)

        # process
        # greedy function
        def canDo(target):
            total = 0
            for x in range(target):
                if x + 1 not in banned:
                    total += (x + 1)
                    if total > maxSum:
                        return False
            return True

        # binary search
        left, right = 1, n
        while left + 1 < right:
            middle = (left + right) // 2
            if canDo(middle):
                left = middle
            else:
                right = middle - 1

        target = left
        if canDo(right):
            target = right

        # post-process
        ans = 0
        for x in range(target):
            if x + 1 not in banned:
                ans += 1
        return ans


banned = [1,6,5]
n = 5
maxSum = 6

banned = [1,2,3,4,5,6,7]
n = 8
maxSum = 1

banned = [11]
n = 7
maxSum = 50

solution = Solution()
print(solution.maxCount(banned, n, maxSum))

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        left = 1
        right = k + 1

        # process
        ans = list()
        count = 0
        while left <= right:
            if count % 2 == 0:
                ans.append(left)
                left += 1
            else:
                ans.append(right)
                right -= 1
            count += 1

        for x in range(k + 1, n):
            ans.append(x + 1)

        return ans


n = 3
k = 1

n = 3
k = 2

"""
n = 100
k = 10
"""

solution = Solution()
print(solution.constructArray(n, k))

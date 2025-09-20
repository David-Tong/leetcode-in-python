class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        # process
        total = n * n * w
        ans = 0
        if total > maxWeight:
            ans = maxWeight // w
        else:
            ans = n * n
        return ans


n = 2
w = 3
maxWeight = 15

n = 3
w = 5
maxWeight = 20

solution = Solution()
print(solution.maxContainers(n, w, maxWeight))

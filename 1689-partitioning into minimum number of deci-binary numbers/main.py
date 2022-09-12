class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        ans = 0
        for ch in n:
            ans = max(int(ch), ans)
            if ans == 9:
                return 9
        return ans


n = "32"
n = "82734"
n = "27346209830709182346"
n = "1000000200005"

solution = Solution()
print(solution.minPartitions(n))

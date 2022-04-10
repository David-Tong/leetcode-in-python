class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        num = n
        while num not in visited:
            visited.add(num)
            sumi = 0
            for x in str(num):
                sumi += int(x) ** 2
            num = sumi
            if num == 1:
                return True
        return False


n = 19
n = 2
n = 1

solution = Solution()
print(solution.isHappy(n))

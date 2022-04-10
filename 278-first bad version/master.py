# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isBadVersion(middle):
            bad = 1000
            if middle >= bad:
                return True
            else:
                return False

        left = 1
        right = n
        while left + 1 < right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle

        if isBadVersion(left):
            return left
        else:
            return right


n = 5
n = 1
n = 1000
solution = Solution()
print(solution.firstBadVersion(n))

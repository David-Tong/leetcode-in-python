class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True

        x = str(x)
        L = len(x)
        if L % 2 == 1:
            left = L // 2
            right = L // 2
        else:
            left = L // 2 - 1
            right = L // 2

        while left >= 0 and right < L:
            if x[left] == x[right]:
                left -= 1
                right += 1
            else:
                return False
        return True


x = 121
x = -121
x = 10
x = 22
x = 3
x = 0

solution = Solution()
print(solution.isPalindrome(x))

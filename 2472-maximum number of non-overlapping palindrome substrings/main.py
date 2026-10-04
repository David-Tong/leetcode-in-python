import string


class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(s)

        # count all intervals match conditions
        # 1 - the interval is palindromic
        # 2 - with the length larger than k
        intervals = list()

        # odd length palindrome
        for center in range(L):
            left = right = center
            while left >= 0 and right < L and s[left] == s[right]:
                length = right - left + 1
                if length >= k:
                    intervals.append((left, right))
                    break
                left -= 1
                right += 1

        # even length palindrome
        for center in range(L):
            left, right = center, center + 1
            while left >= 0 and right < L and s[left] == s[right]:
                length = right - left + 1
                if length >= k:
                    intervals.append((left, right))
                    break
                left -= 1
                right += 1

        # process
        # sort intervals by its right point
        intervals.sort(key=lambda x: x[1])
        # print(intervals)

        # greedy algorithm
        ans = 0
        last = -1
        for left, right in intervals:
            if left > last:
                ans += 1
                last = right
        return ans


s = "abaccdbbd"
k = 3

s = "adbcda"
k = 2

s = "aaaaaaaaa"
k = 3

from random import choice
s = "".join(choice(string.lowercase) for _ in range(2000))
k = 100
print(s)

solution = Solution()
print(solution.maxPalindromes(s, k))

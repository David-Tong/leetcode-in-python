class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        for digit in num:
            dicts[digit] += 1

        odds = list()
        evens = defaultdict(int)

        for digit in dicts:
            if dicts[digit] % 2 == 1:
                odds.append(digit)
                if dicts[digit] > 1:
                    evens[digit] = (dicts[digit] - 1) // 2
            else:
                evens[digit] = dicts[digit] // 2

        # process
        palindrome = ""
        if evens and sorted(evens.keys())[-1] != "0":
            for digit in sorted(evens.keys(), reverse=True):
                palindrome += digit * evens[digit]
        else:
            if len(odds) == 0:
                return 0

        if len(odds) != 0:
            ans = palindrome + max(odds) + palindrome[::-1]
        else:
            ans = palindrome + palindrome[::-1]

        return ans


num = "444947137"
num = "00009"
num = "1328642378691203748647902357127847890571920749182790578129748192047129847120947829047129047819284789189478231478277847412847"
num = "9"
num = "0"
num = "00"
num = "99"

solution = Solution()
print(solution.largestPalindromic(num))

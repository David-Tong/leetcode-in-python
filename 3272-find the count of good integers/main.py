from stringold import lower


class Solution(object):
    def countGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # pre-process
        # helper function - make palindromic
        def makePalindrome(num, even):
            res = ""
            if even:
                res = str(num) + str(num)[::-1]
            else:
                res = str(num) + str(num)[:-1][::-1]
            return int(res)

        # print(makePalindrome(12, True))
        # print(makePalindrome(123, False))

        # help function - count rearranged combination
        def countRearrangedCombination(palindrome):
            palindrome = str(palindrome)
            L = len(palindrome)
            from collections import defaultdict
            dicts = defaultdict(int)
            for ch in palindrome:
                dicts[ch] += 1

            from math import factorial
            res = factorial(L)
            for ch in dicts:
                res /= factorial(dicts[ch])

            zeros = 0
            if dicts['0'] > 0:
                zeros = factorial(L - 1)
                for ch in dicts:
                    if ch == '0':
                        zeros /= factorial(dicts[ch] - 1)
                    else:
                        zeros /= factorial(dicts[ch])
            res -= zeros
            return res

        # print(countRearrangedCombination(515))

        # helper function - check duplication
        def checkDuplication(palindrome):
            from collections import defaultdict
            dicts = defaultdict(int)
            palindrome = str(palindrome)
            for ch in palindrome:
                dicts[ch] += 1
            res = ""
            for ch in sorted(dicts):
                res += ch + str(dicts[ch])
            return res
        # print(checkDuplication("12321"))

        # process
        if n % 2 == 0:
            digit = n // 2
            even = True
        else:
            digit = n // 2 + 1
            even = False
        if digit == 1:
            lower = 1
        else:
            lower = 10 ** (digit - 1)
        upper = 10 ** digit
        ans = 0
        palindromes = set()
        for x in range(lower, upper):
            palindrome = makePalindrome(x, even)
            if palindrome % k == 0:
                gene = checkDuplication(palindrome)
                if gene not in palindromes:
                    palindromes.add(gene)
                    ans +=  countRearrangedCombination(palindrome)
        return ans


n = 3
k = 5

n = 1
k = 4

n = 5
k = 6


solution = Solution()
print(solution.countGoodIntegers(n, k))

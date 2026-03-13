class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        NUMBERS = [''] + [str(_) for _ in range(10)]
        PALINDROMES = set()
        LIMIT = 10 ** 9

        def makePalindrome(num):
            palindromes = list()
            if num[-1] != '0':
                if len(num) > 1:
                    palindrome = num[1:][::-1] + num[0] + num[1:]
                    palindrome = int(palindrome)
                    if palindrome <= LIMIT:
                        palindromes.append(palindrome)
                else:
                    palindromes.append(int(num))
                palindrome = num[::-1] + num
                palindrome = int(palindrome)
                if palindrome <= LIMIT:
                    palindromes.append(palindrome)
            return palindromes

        def isPrime(num):
            if num == 1:
                return False
            from math import sqrt
            for x in range(2, int(sqrt(num)) + 1):
                if num % x == 0:
                    return False
            return True

        for x in NUMBERS:
            for y in NUMBERS:
                for z in NUMBERS:
                    for i in NUMBERS:
                       for j in NUMBERS:
                           num = '{}{}{}{}{}'.format(x, y, z, i, j)
                           if num:
                                # print(num)
                                PALINDROMES.update(makePalindrome(num))
        PALINDROMES = sorted(PALINDROMES)
        # print(PALINDROMES)
        print(len(PALINDROMES))

        # process
        from bisect import bisect_left
        idx = bisect_left(PALINDROMES, n)

        while idx < len(PALINDROMES):
            if isPrime(PALINDROMES[idx]):
                return PALINDROMES[idx]
            idx += 1
        return None


n = 6
n = 8
n = 13
n = 10000
n = 10 ** 8
n = 2
n = 1
n = 9938400

solution = Solution()
print(solution.primePalindrome(n))

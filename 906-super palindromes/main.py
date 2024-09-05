class Solution(object):
    def superpalindromesInRange(self, left, right):
        """
        :type left: str
        :type right: str
        :rtype: int
        """
        def isPalindrome(number):
            number = str(number)

            left = 0
            right = len(number) - 1
            while left < right:
                if number[left] != number[right]:
                    return False
                left += 1
                right -= 1
            return True

        # generate palindromes
        palindromes = set()
        for x in range(3):
            palindromes.add(x + 1)

        def generatePalindromes(number):
            if len(number) == 5:
                number = str(int(number))
                if len(number) == 1:
                    if int(number) != 0:
                        palindromes.add(int(number * 2))
                else:
                    palindromes.add(int(number + number[::-1]))
                    palindromes.add(int(number[:-1] + number[-1] + number[:-1][::-1]))
            else:
                for x in range(3):
                    generatePalindromes(number + str(x))

        generatePalindromes("")

        # generate super palindrome
        superpalindrome = set()
        for palindrome in palindromes:
            powed = pow(palindrome, 2)
            if isPalindrome(powed):
                superpalindrome.add(powed)
        superpalindrome = sorted(superpalindrome)

        # search
        from bisect import bisect_left, bisect_right
        idx = bisect_left(superpalindrome, int(left))
        idx2 = bisect_right(superpalindrome, int(right))
        return idx2 - idx


left = "4"
right = "484"

left = "1"
right = "2"

solution = Solution()
print(solution.superpalindromesInRange(left, right))
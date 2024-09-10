class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        # pre-process
        L = len(n)

        def constructPalindrome(n):
            number = [''] * L
            left = 0
            right = L - 1
            # construct palindrome by copy the first half to the second half
            while left <= right:
                number[left] = n[left]
                number[right] = n[left]
                left += 1
                right -= 1
            return "".join(number)

        def nextSmaller(n):
            # if the constructed palindrome is less than n, return it
            palindrome = constructPalindrome(n)
            if palindrome < n:
                return palindrome

            # calculate the smaller palindrome
            palindrome = list(palindrome)
            carry = 1
            idx = (L - 1) // 2
            while idx >= 0:
                d = int(n[idx]) - carry
                if d >= 0:
                    palindrome[idx] = str(d)
                    carry = 0
                else:
                    palindrome[idx] = '9'
                    carry = 1
                palindrome[L - 1 - idx] = palindrome[idx]
                idx -= 1

            # conner case when we reduce to a palindrome with length - 1
            if palindrome[0] == '0' and L > 1:
                return '9' * (L - 1)
            else:
                return "".join(palindrome)

        def nextGreater(n):
            # if the constructed palindrome is less than n, return it
            palindrome = constructPalindrome(n)
            if palindrome > n:
                return palindrome

            # calculate the greater palindrome
            palindrome = list(palindrome)
            carry = 1
            idx = (L - 1) // 2
            while idx >= 0:
                d = int(n[idx]) + carry
                if d <= 9:
                    palindrome[idx] = str(d)
                    carry = 0
                else:
                    palindrome[idx] = '0'
                    carry = 1
                palindrome[L - 1 - idx] = palindrome[idx]
                idx -= 1

            # conner case when we increase to a palindrome with length + 1
            if carry:
                return '1' + '0' * (L - 1) + '1'
            else:
                return "".join(palindrome)

        # process
        smaller = nextSmaller(n)
        greater = nextGreater(n)

        print(smaller, greater)

        if int(greater) - int(n) < int(n) - int(smaller):
            return greater
        else:
            return smaller


n = "123"
n = "1"
n = "12399"
n = "39512"
n = "991"
n = "1004"
n = "999"


solution = Solution()
print(solution.nearestPalindromic(n))

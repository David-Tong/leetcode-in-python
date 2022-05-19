class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        M = len(a)
        N = len(b)

        i = M - 1
        j = N - 1
        carry = 0
        ans = ""
        while i >= 0 and j >= 0:
            digit1 = int(a[i])
            digit2 = int(b[j])
            total = digit1 + digit2 + carry
            digit = total % 2
            carry = total // 2
            ans = str(digit) + ans
            i -= 1
            j -= 1

        while i >= 0:
            digit1 = int(a[i])
            total = digit1 + carry
            digit = total % 2
            carry = total // 2
            ans = str(digit) + ans
            i -= 1

        while j >= 0:
            digit2 = int(b[j])
            total = digit2 + carry
            digit = total % 2
            carry = total // 2
            ans = str(digit) + ans
            j -= 1

        if carry != 0:
            ans = str(carry) + ans

        return ans


a = "11"
b = "1"

a = "1010"
b = "1011"

a = "1"
b = "1"

a = "100"
b = "110010"

solution = Solution()
print(solution.addBinary(a, b))

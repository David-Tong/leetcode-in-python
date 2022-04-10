class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0

        index1 = 0
        index2 = 0
        ans = ""
        while index1 < len(num1) and index2 < len(num2):
            addon = int(num1[index1]) + int(num2[index2]) + carry
            carry = addon // 10
            ans = str(addon % 10) + ans
            index1 += 1
            index2 += 1

        while index1 < len(num1):
            addon = int(num1[index1]) + carry
            carry = addon // 10
            ans = str(addon % 10) + ans
            index1 += 1
        
        while index2 < len(num2):
            addon = int(num2[index2]) + carry
            carry = addon // 10
            ans = str(addon % 10) + ans
            index2 += 1

        if carry != 0:
            ans = str(carry) + ans

        return ans


num1 = "11"
num2 = "123"

num1 = "456"
num2 = "77"

num1 = "0"
num2 = "0"

num1 = "1"
num2 = "9"

solution = Solution()
print(solution.addStrings(num1, num2))

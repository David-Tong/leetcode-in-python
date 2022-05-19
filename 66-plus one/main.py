class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        N = len(digits)
        carry = 0
        for x in range(N - 1, -1, -1):
            if x == N - 1:
                addon = (digits[x] + 1) % 10
                carry = (digits[x] + 1) // 10
            else:
                addon = (digits[x] + carry) % 10
                carry = (digits[x] + carry) // 10
            digits[x] = addon
            if carry == 0:
                break
        if carry != 0:
            digits = [carry] + digits

        return digits


digits = [1,2,3]
#digits = [4,3,2,1]
#digits = [9]
#digits = [1,9]
digits = [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]


solution = Solution()
print(solution.plusOne(digits))

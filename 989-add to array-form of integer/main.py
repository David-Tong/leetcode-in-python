class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        k = str(k)
        M = len(num)
        N = len(k)

        i = M - 1
        j = N - 1
        carry = 0
        result = ""
        while i >= 0 and j >= 0:
            total = num[i] + int(k[j]) + carry
            digit = total % 10
            carry = total // 10
            result = str(digit) + result
            i -= 1
            j -= 1

        while i >= 0:
            total = num[i] + carry
            digit = total % 10
            carry = total // 10
            result = str(digit) + result
            i -= 1

        while j >= 0:
            total = int(k[j]) + carry
            digit = total % 10
            carry = total // 10
            result = str(digit) + result
            j -= 1

        if carry != 0:
            result = str(carry) + result

        ans = []
        for x in range(len(result)):
            ans.append(int(result[x]))
        return ans


num = [1,2,0,0]
k = 34

num = [2,7,4]
k = 181

num = [2,1,5]
k = 806

num = [1]
k = 999999

solution = Solution()
print(solution.addToArrayForm(num, k))

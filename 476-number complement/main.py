class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bits = list()
        while num:
            if num & 1:
                bits.append(0)
            else:
                bits.append(1)
            num >>= 1

        ans = 0
        for idx, bit in enumerate(bits):
            ans += 2 ** idx * bit
        return ans


num = 5
num = 1
num = 1000555

solution = Solution()
print(solution.findComplement(num))

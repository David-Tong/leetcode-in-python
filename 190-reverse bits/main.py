class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        sum = 0
        for x in range(32):
            sum += (n >> x & 1) * pow(2, 32 - x - 1)
        return sum


n = 0b00000010100101000001111010011100
n = 0b11111111111111111111111111111101

solution = Solution()
print(solution.reverseBits(n))

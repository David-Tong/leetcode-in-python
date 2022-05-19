class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        idx = 0
        while idx < len(bits):
            if idx == len(bits) - 1:
                return True
            if bits[idx] == 0:
                idx += 1
            else:
                idx += 2
        return False


bits = [1,0,0]
bits = [1,1,1,0]
bits = [0]

solution = Solution()
print(solution.isOneBitCharacter(bits))

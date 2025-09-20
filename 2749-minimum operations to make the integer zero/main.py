class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        # process
        # minimize k
        #   s.t. num1 - k * num2 = sum_k(2 ** i) >= k
        #        num1 >= k * (num2 + 1)
        x, y = num1, num2

        k = 1
        while True:
            x -= y
            if x < k:
                return -1
            count = bin(x).count("1")
            # sum_k(2 ** i) can construct any number with less than k 1 in its binary
            if count <= k:
                return k
            k += 1


num1 = 3
num2 = -2

solution = Solution()
print(solution.makeTheIntegerZero(num1, num2))

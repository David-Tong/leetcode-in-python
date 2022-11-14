class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def get_ones(bin):
            ones = 0
            for ch in bin:
                if ch == "1":
                    ones += 1
            return ones

        bin1 = bin(num1)[2:]
        bin2 = bin(num2)[2:]

        ones1 = get_ones(bin1)
        ones2 = get_ones(bin2)

        if ones1 == ones2:
            return num1
        else:
            bin3 = list()
            for ch in bin1:
                bin3.append(ch)
            if ones1 > ones2:
                count = ones1 - ones2
                for x in range(len(bin3) - 1, -1, -1):
                    if bin3[x] == "1":
                        bin3[x] = "0"
                        count -= 1
                    if count == 0:
                        break
            elif ones1 < ones2:
                count = ones2 - ones1
                for x in range(len(bin3) - 1, -1, -1):
                    if bin3[x] == "0":
                        bin3[x] = "1"
                        count -= 1
                    if count == 0:
                        break
                if count > 0:
                    bin3 = ["1"] * count + bin3

            num3 = int("".join(bin3), 2)
            return num3


num1 = 3
num2 = 5

num1 = 1
num2 = 12

num1 = 12
num2 = 1

solution = Solution()
print(solution.minimizeXor(num1, num2))
class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        head = 0
        for digit in str(num)[:-1]:
            head += int(digit)
        tail = str(num)[-1]

        if int(head) % 2 == 0:
            return num // 2
        else:
            if int(tail) % 2 == 0:
                return num // 2 - 1
            else:
                return num // 2


num = 4
#num = 30
#num = 100
#num = 1000
#num = 1
#num = 21
#num = 910

solution = Solution()
print(solution.countEven(num))
class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def doCount(num1, num2, count):
            if num1 == 0 or num2 == 0:
                return count

            if num1 >= num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1

            return doCount(num1, num2, count + 1)

        return doCount(num1, num2, 0)


num1 = 2
num2 = 3

num1 = 10
num2 = 10

num1 = 0
num2 = 10

solution = Solution()
print(solution.countOperations(num1, num2))

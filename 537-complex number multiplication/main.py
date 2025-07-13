class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # pre-process
        def parse(num):
            nums = num.split("+")
            a, b = int(nums[0]), int(nums[1][:-1])
            return a, b

        # print(parse(num1))
        # print(parse(num2))

        a1, b1 = parse(num1)
        a2, b2 = parse(num2)

        # process
        a = a1 * a2 - b1 * b2
        b = a1 * b2 + a2 * b1
        ans = "{}+{}i".format(a, b)
        return ans


num1 = "1+1i"
num2 = "1+1i"

num1 = "1+-1i"
num2 = "1+-1i"

num1 = "1+0i"
num2 = "1+-1i"

solution = Solution()
print(solution.complexNumberMultiply(num1, num2))

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = list()
        for x in range(1, n + 1):
            if x % 5 == 0:
                if x % 3 == 0:
                    ans.append("FizzBuzz")
                else:
                    ans.append("Buzz")
            else:
                if x % 3 == 0:
                    ans.append("Fizz")
                else:
                    ans.append(str(x))
        return ans


n = 100

solution = Solution()
print(solution.fizzBuzz(n))

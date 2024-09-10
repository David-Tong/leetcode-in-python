class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        factors = sorted([a, b, c])

        def gcd(num, num2):
            return num if num2 == 0 else gcd(num2, num % num2)

        def lcm(num, num2):
            return num * num2 / gcd(num, num2)

        def hasUgly(target):
            ugly = target // factors[0] + target // factors[1] + target // factors[2] \
                - target // lcm(factors[0], factors[1]) - target // lcm(factors[0], factors[2]) - target // lcm(factors[1], factors[2]) \
                + target // lcm(factors[0], lcm(factors[1], factors[2]))

            if ugly >= n:
                return True
            else:
                return False

        left = 1
        right = 2 * 10 ** 9

        while left + 1 < right:
            middle = (left + right) // 2
            if hasUgly(middle):
                right = middle
            else:
                left = middle + 1

        if hasUgly(left):
            return left
        else:
            return right


n = 3
a = 2
b = 3
c = 5

n = 4
a = 2
b = 3
c = 4

n = 5
a = 2
b = 11
c = 13

n = 15
a = 10
b = 100
c = 1000

n = 5
a = 2
b = 3
c = 3

n = 10
a = 7
b = 6
c = 8

solution = Solution()
print(solution.nthUglyNumber(n, a, b, c))

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def gcd(p, q):
            if p % q == 0:
                return q
            else:
                return gcd(q, p % q)

        def lcm(p, q):
            return p * q // gcd(p, q)

        if q == 0:
            return 0
        else:
            total = lcm(p, q)
            times = total // q
            if times % 2 == 1:
                if (total // p) % 2 == 0:
                    return 0
                else:
                    return 1
            else:
                return 2


p = 2
q = 1

p = 3
q = 1

p = 10
q = 3

p = 100
q = 21

p = 100
q = 20

solution = Solution()
print(solution.mirrorReflection(p, q))

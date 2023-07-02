class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MODULO = 1337
        L = len(b)

        # start calculation
        a = a % MODULO
        ans = 1
        for x in range(L):
            ans = pow(ans, 10) * pow(a, b[x]) % MODULO
        return ans


a = 2
b = [3]

a = 2
b = [1,0]

a = 1
b = [4, 3, 3, 8, 5, 2]

a = 83726
b = [4, 3, 3, 8, 5, 2]

solution = Solution()
print(solution.superPow(a, b))


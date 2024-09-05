class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        bin_a = bin(a)[2:]
        bin_b = bin(b)[2:]
        bin_c = bin(c)[2:]

        L = max(len(bin_a), max(len(bin_b), len(bin_c)))
        bin_a = '0' * (L - len(bin_a)) + bin_a
        bin_b = '0' * (L - len(bin_b)) + bin_b
        bin_c = '0' * (L - len(bin_c)) + bin_c

        ans = 0
        for x in range(L):
            if bin_c[x] == '1':
               if bin_a[x] == '0' and bin_b[x] == '0':
                   ans += 1
            elif bin_c[x] == '0':
                if bin_a[x] == '1':
                    ans += 1
                if bin_b[x] == '1':
                    ans += 1
        return ans


a = 2
b = 6
c = 5

a = 4
b = 2
c = 7

a = 1
b = 2
c = 3

a = 10445812
b = 19488235
c = 1837

solution = Solution()
print(solution.minFlips(a, b, c))

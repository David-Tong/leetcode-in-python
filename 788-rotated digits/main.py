class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        L = len(str(n))

        def selectedDigits(n):
            # zeros - the number of selected digits for rotate to themselves
            # ones - the number of selected digits for rotate to others
            if n < 0:
                zeros = 0
            elif n < 1:
                zeros = 1
            elif n < 8:
                zeros = 2
            else:
                zeros = 3

            if n < 2:
                ones = 0
            elif n < 5:
                ones = 1
            elif n < 6:
                ones = 2
            elif n < 9:
                ones = 3
            else:
                ones = 4

            return (zeros, ones)

        # dicts[x][0] - the number of good numbers included in the xth digits of number, when the xth digit is rotate to others
        #      [x][1] - the number of good numbers included in the xth digits of number, when the xth digit is rotate to themselves
        dicts = [[0] * 2 for _ in range(L)]
        dicts[0][0] = 4
        dicts[0][1] = 7

        for x in range(1, L):
            dicts[x][0] = 3 * dicts[x - 1][0] + 4 * dicts[x - 1][1]
            dicts[x][1] = 7 ** (x + 1)

        ans = 0
        wasOnes = False

        for x in range(L):
            digit = int(str(n)[x])

            if x == L - 1:
                zeros, ones = selectedDigits(digit)
                if wasOnes:
                    ans += (zeros + ones)
                else:
                    ans += ones
            else:
                zeros, ones = selectedDigits(digit - 1)
                if wasOnes:
                    ans += zeros * dicts[L - x - 2][1] + ones * dicts[L - x - 2][1]
                else:
                    ans += zeros * dicts[L - x - 2][0] + ones * dicts[L - x - 2][1]

            if digit in [2, 5, 6, 9]:
                wasOnes = True
            elif digit in [3, 4, 7]:
                break

        return ans


n = 10
n = 1
n = 2
n = 99
n = 987
n = 999
n = 9886
n = 10000
n = 459

solution = Solution()
print(solution.rotatedDigits(n))

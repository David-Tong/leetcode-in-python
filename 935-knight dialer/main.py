class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        # dp
        curr = [1] * 10

        for x in range(n - 1):
            old = curr
            curr = list()
            # 0
            curr.append(old[4] + old[6])
            # 1
            curr.append(old[6] + old[8])
            # 2
            curr.append(old[7] + old[9])
            # 3
            curr.append(old[4] + old[8])
            # 4
            curr.append(old[0] + old[3] + old[9])
            # 5
            curr.append(0)
            # 6
            curr.append(old[0] + old[1] + old[7])
            # 7
            curr.append(old[2] + old[6])
            # 8
            curr.append(old[1] + old[3])
            # 9
            curr.append(old[2] + old[4])

        return sum(curr) % MODULO


n = 1
n = 3
n = 3131


solution = Solution()
print(solution.knightDialer(n))

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base case
        if n <= 3:
            return 1

        magic = [1, 2, 2]
        idx = 2

        # create magic string
        while idx < n:
            if magic[-1] == 1:
                num = 2
            else:
                num = 1
            if magic[idx] == 1:
                magic.append(num)
            else:
                magic.append(num)
                magic.append(num)
            idx += 1

        # count ones
        ans = 0
        for num in magic[:n]:
            if num == 1:
                ans += 1
        return ans


n = 10
n = 1
n = 10 ** 5

solution = Solution()
print(solution.magicalString(n))

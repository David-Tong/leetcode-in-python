class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        L = len(arr)
        presums = [0]
        for num in arr:
            presums.append(presums[-1] + num)
        # print(presums)

        # process
        odds, evens = 0, 0
        ans = 0
        for x in range(L + 1):
            if x == 0:
                if presums[x] % 2 == 0:
                    evens += 1
                else:
                    odds += 1
            else:
                if presums[x] % 2 == 0:
                    ans += odds
                    evens += 1
                else:
                    ans += evens
                    odds += 1
        ans = ans % MODULO
        return ans


arr = [1,3,5]
arr = [2,4,6]
arr = [1,2,3,4,5,6,7]

solution = Solution()
print(solution.numOfSubarrays(arr))

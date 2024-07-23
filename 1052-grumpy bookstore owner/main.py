class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        # pre-process
        L = len(customers)
        presums = [0]
        for x in range(L):
            presums.append(presums[-1] + customers[x] * grumpy[x])

        # process
        maxi = 0
        for x in range(minutes, L + 1):
            maxi = max(maxi, presums[x] - presums[x - minutes])

        ans = sum(customers) - (presums[-1] - maxi)
        return ans


customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3

customers = [1]
grumpy = [0]
minutes = 1

solution = Solution()
print(solution.maxSatisfied(customers, grumpy, minutes))

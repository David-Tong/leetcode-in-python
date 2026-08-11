class Solution(object):
    def sumOfLargestPrimes(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)

        # helper function
        def isPrime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False

            idx = 5
            while idx ** 2 <= num:
                if num % idx == 0 or num % (idx + 2) == 0:
                    return False
                idx += 6

            return True

        # process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for x in range(L):
            for y in range(x + 1, L + 1):
                num = int(s[x: y])
                if isPrime(num):
                    # print(num)
                    if num not in heap:
                        heappush(heap, num)
                        while len(heap) > 3:
                            heappop(heap)

        # post-process
        ans = 0
        while heap:
            ans += heappop(heap)
        return ans


s = "12234"
s = "111"
s = "9983672364"
s = "2"

solution = Solution()
print(solution.sumOfLargestPrimes(s))

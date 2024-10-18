class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        # pre-process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        if a > 0:
            heappush(heap, (a * -1, 'a'))
        if b > 0:
            heappush(heap, (b * -1, 'b'))
        if c > 0:
            heappush(heap, (c * -1, 'c'))

        # process
        ans = ''
        while heap:
            num, ch = heappop(heap)
            num *= -1
            if ans and ans[-1] == ch:
                ans += ch
                num -= 1
            else:
                if num > 2:
                    ans += ch * 2
                    num -= 2
                else:
                    ans += ch * num
                    num = 0
            if not heap:
                return ans
            else:
                num2, ch2 = heappop(heap)
                num2 *= -1
                ans += ch2
                if num > 0:
                    heappush(heap, (num * -1, ch))
                if num2 > 1:
                    heappush(heap, (1 - num2, ch2))
        return ans


a = 1
b = 1
c = 7

a = 7
b = 1
c = 0

a = 7
b = 7
c = 7

a = 4
b = 4
c = 3

solution = Solution()
print(solution.longestDiverseString(a, b, c))

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        # pre-process
        # helper function
        def isValid(num, num2, num3):
            if abs(num - num2) <= a:
                if abs(num2 - num3) <= b:
                    if abs(num - num3) <= c:
                        return True
            return False

        # process
        L = len(arr)
        ans = 0
        for x in range(L):
            for y in range(x + 1, L):
                for z in range(y + 1, L):
                    if isValid(arr[x], arr[y], arr[z]):
                        ans += 1
        return ans


arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3

arr = [1,1,2,2,3]
a = 0
b = 0
c = 1

solution = Solution()
print(solution.countGoodTriplets(arr, a, b, c))

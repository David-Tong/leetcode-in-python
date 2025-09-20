class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        # helper function
        # gcd
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # process
        stack = list()
        for num in nums:
            n = num
            while stack:
                g = gcd(stack[-1], n)
                if g > 1:
                    num2 = stack.pop()
                    n = n * num2 // g
                else:
                    break
            stack.append(n)
        ans = stack
        return ans


nums = [6,4,3,2,7,6,2]
nums = [2,2,1,1,3,3,3]

solution = Solution()
print(solution.replaceNonCoprimes(nums))

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def doCountAndSay(n):
            if n == 1:
                return "1"

            nums = doCountAndSay(n-1)
            groups = []
            left = 0
            right = 0
            while right < len(nums):
                if nums[right] == nums[left]:
                    right += 1
                else:
                    groups.append((nums[left], right - left))
                    left = right
                    right += 1
            groups.append((nums[left], right - left))

            ans = ""
            for num, count in groups:
                ans += str(count) + num
            return ans

        return doCountAndSay(n)


n = 1
n = 2
n = 3
n = 4
n = 30

solution = Solution()
print(solution.countAndSay(n))

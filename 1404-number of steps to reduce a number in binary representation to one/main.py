class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        from collections import deque
        nums = deque()
        for digit in s[::-1]:
            nums.append(int(digit))

        # process
        ans = 0
        while len(nums) > 1:
            if nums[0] == 0:
                # rule 1
                nums.popleft()
            else:
                # rule 2
                addon = 1
                for x in range(len(nums)):
                    nums[x] += addon
                    if nums[x] > 1:
                        nums[x] = 0
                        addon = 1
                    else:
                        addon = 0
                        break
                if addon > 0:
                    nums.append(addon)
            ans += 1
        return ans


s = "1101"
s = "10"
s = "1"
s = "10101010110011001111111101010111111111111111111000001111111111111111111111111111111001111011111111111111111111111001111101"

solution = Solution()
print(solution.numSteps(s))

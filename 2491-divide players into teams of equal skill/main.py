from string import rindex


class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        # pre-process
        L = len(skill)
        total = sum(skill)
        if L % 2 != 0 or total % (L // 2) != 0:
            return -1
        target = total // (L // 2)

        # process
        skill = sorted(skill)
        left = 0
        right = L - 1
        ans = 0
        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            else:
                ans += skill[left] * skill[right]
                left += 1
                right -= 1
        return ans


skill = [3,2,5,1,3,4]
skill = [3,4]
skill = [1,1,2,3]
skill = [1000,100,5,6,12,34]

solution = Solution()
print(solution.dividePlayers(skill))

class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        # pre-process
        L = len(energy)

        def canEnergyWin(target):
            init = initialEnergy + target
            for x in range(L):
                if init <= energy[x]:
                    return False
                else:
                    init -= energy[x]
            return True

        def canExperienceWin(target):
            init = initialExperience + target
            for x in range(L):
                if init <= experience[x]:
                    return False
                else:
                    init += experience[x]
            return True

        # binary search
        left = 0
        right = 10 ** 5

        while left + 1 < right:
            middle = (left + right) // 2
            if canEnergyWin(middle):
                right = middle
            else:
                left = middle + 1

        if canEnergyWin(left):
            needEnergy = left
        else:
            needEnergy = right

        left = 0
        right = 10 ** 5

        while left + 1 < right:
            middle = (left + right) // 2
            if canExperienceWin(middle):
                right = middle
            else:
                left = middle + 1

        if canExperienceWin(left):
            needExperience = left
        else:
            needExperience = right

        ans = needEnergy + needExperience
        return ans


initialEnergy = 5
initialExperience = 3
energy = [1,4,3,2]
experience = [2,6,3,1]

initialEnergy = 2
initialExperience = 4
energy = [1]
experience = [3]

solution = Solution()
print(solution.minNumberOfHours(initialEnergy, initialExperience, energy, experience))

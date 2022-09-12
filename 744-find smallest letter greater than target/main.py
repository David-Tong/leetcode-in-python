class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters) - 1

        while left + 1 < right:
            middle = (left + right) // 2
            if ord(letters[middle]) > ord(target):
                right = middle - 1
            else:
                left = middle + 1

        idx = 0
        if ord(target) < ord(letters[left]):
            idx = left
        elif ord(target) < ord(letters[right]):
            idx = right
        else:
            idx = right + 1

        if idx == len(letters):
            idx = 0

        return letters[idx]


letters = ["c","c","f","j"]
target = "a"
target = "c"
#target = "d"
#target = "z"

solution = Solution()
print(solution.nextGreatestLetter(letters, target))

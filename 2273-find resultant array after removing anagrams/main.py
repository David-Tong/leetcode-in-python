class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def isAnagrams(word, word2):
            if len(word) == len(word2):
                if sorted(word) == sorted(word2):
                    return True
            return False

        slow = 0
        fast = 1

        ans = list()
        while fast < len(words):
            if isAnagrams(words[slow], words[fast]):
                fast += 1
            else:
                ans.append(words[slow])
                slow = fast
                fast += 1
        ans.append(words[slow])
        return ans


words = ["abba","baba","bbaa","cd","cd"]
words = ["a","b","c","d","e"]
words = ["abba", "baba", "bbaa", "aabb", "baab", "abab"]
words = ["aa"]

solution = Solution()
print(solution.removeAnagrams(words))

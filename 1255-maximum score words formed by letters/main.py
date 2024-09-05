class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        # pre-process
        from copy import deepcopy
        L = len(words)
        from collections import defaultdict
        availables = defaultdict(int)
        for letter in letters:
            availables[letter] += 1

        def scoreWords(idx, availables):
            if idx == L:
                return 0

            saved_availables = deepcopy(availables)
            word = words[idx]

            selected = True
            for ch in word:
                if availables[ch] > 0:
                    availables[ch] -= 1
                else:
                    selected = False
                    break

            # not selected
            ans = scoreWords(idx + 1, saved_availables)
            if selected:
                add_score = 0
                for ch in word:
                    add_score += score[ord(ch) - ord('a')]
                ans = max(ans, scoreWords(idx + 1, availables) + add_score)
            return ans

        return scoreWords(0, availables)


words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

words = ["xxxz","ax","bx","cx"]
letters = ["z","a","b","c","x","x","x"]
score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]

words = ["leetcode"]
letters = ["l","e","t","c","o","d"]
score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]

words = ["a", "ax", "az", "bzs", "aa", "dd", "cd", "cc", "adt", "xyz", "bgh", "cc", "fuc", "adr"]
letters = ["a", "b", "c", "d", "f", "u", "r", "x", "y", "z"]
score = [10,2,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,1,1]

solution = Solution()
print(solution.maxScoreWords(words, letters, score))

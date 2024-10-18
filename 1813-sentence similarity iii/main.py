from re import match


class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        # pre-process
        s1, s2 = sentence1.split(), sentence2.split()
        L1, L2 = len(s1), len(s2)

        if L1 > L2:
            s1, s2 = s2, s1
            L1, L2 = L2, L1

        # process
        for bar in range(L1 + 1):
            # check prefix - s1[:bar]
            idx1, idx2 = 0, 0
            matched = True
            while idx1 < bar:
                if s1[idx1] != s2[idx2]:
                    matched = False
                    break
                idx1 += 1
                idx2 += 1

            # check suffix - s1[bar:]
            if matched:
                idx1, idx2 = L1 - 1, L2 - 1
                while idx1 >= bar:
                    if s1[idx1] != s2[idx2]:
                        matched = False
                        break
                    idx1 -= 1
                    idx2 -= 1

            if matched:
                return True

        return False


sentence1 = "My name is Haley"
sentence2 = "My Haley"

sentence1 = "of"
sentence2 = "A lot of words"

sentence1 = "Eating right now"
sentence2 = "Eating"

"""
sentence1 = "This is a china toy tank"
sentence2 = "This is a toy"

sentence1 = "Luky"
sentence2 = "Lucccky"

sentence1 = "UI wqhw Lf"
sentence2 = "ezzXqqEQcS"

sentence1 = "A"
sentence2 = "a A b A"

sentence1 = "Db C"
sentence2 = "C Db"

sentence1 = "bb aa aa bb"
sentence2 = "aa bb"
"""

solution = Solution()
print(solution.areSentencesSimilar(sentence1, sentence2))

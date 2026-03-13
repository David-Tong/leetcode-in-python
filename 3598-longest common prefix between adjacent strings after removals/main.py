class Solution(object):
    def longestCommonPrefix(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        # pre-process
        # conner cases
        L = len(words)
        if L == 1:
            ans = [0]
            return ans
        elif L == 2:
            ans = [0, 0]
            return ans

        # helper function
        def commonPrefix(word, word2):
            W = min(len(word), len(word2))
            idx = 0
            while idx < W:
                if word[idx] != word2[idx]:
                    return idx
                idx += 1
            return idx

        from collections import defaultdict
        dicts = defaultdict(int)

        from sortedcontainers import SortedList
        sl = SortedList()

        L = len(words)
        idx = 0
        while idx < L - 1:
            key = "{}-{}".format(idx, idx + 1)
            dicts[key] = commonPrefix(words[idx], words[idx + 1])
            sl.add(dicts[key])
            idx += 1

        # print(dicts)
        # print(sl)

        # process
        idx = 0
        ans = list()
        while idx < L:
            if 0 < idx < L - 1:
                # remove left
                left = "{}-{}".format(idx - 1, idx )
                sl.remove(dicts[left])
                # remove right
                right = "{}-{}".format(idx, idx + 1)
                sl.remove(dicts[right])
                # update
                temp = commonPrefix(words[idx - 1], words[idx + 1])
                sl.add(temp)
                ans.append(sl[-1])
                sl.remove(temp)
                # add left
                left = "{}-{}".format(idx - 1, idx)
                sl.add(dicts[left])
                # add right
                right = "{}-{}".format(idx, idx + 1)
                sl.add(dicts[right])
            elif idx == 0:
                # remove right
                right = "{}-{}".format(idx, idx + 1)
                sl.remove(dicts[right])
                # update
                ans.append(sl[-1])
                # add right
                right = "{}-{}".format(idx, idx + 1)
                sl.add(dicts[right])
            else:
                # remove left
                left = "{}-{}".format(idx - 1, idx)
                sl.remove(dicts[left])
                # update
                ans.append(sl[-1])
                # add left
                left = "{}-{}".format(idx - 1, idx)
                sl.add(dicts[left])
            idx += 1
        return ans


words = ["jump","run","run","jump","run"]
words = ["dog","racer","car"]
words = ["cdbff"]

solution = Solution()
print(solution.longestCommonPrefix(words))

class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        # pre-process
        # helper function
        VOWELS = "aeiou"
        def convert(word):
            res = ""
            for ch in word:
                if ch in VOWELS:
                    res += "*"
                else:
                    res += ch
            return res

        from collections import defaultdict
        words = set()
        dicts = defaultdict(list)
        changed = defaultdict(list)
        for word in wordlist:
            words.add(word)
            dicts[word.lower()].append(word)
            changed[convert(word.lower())].append(word)

        # print(words)
        # print(dicts)
        # print(changed)

        # process
        ans = list()
        for query in queries:
            # the query exactly matches a word in the wordlist (case-sensitive)
            if query in words:
                ans.append(query)
            # the query matches a word up to capitlization
            elif query.lower() in dicts:
                ans.append(dicts[query.lower()][0])
            # the query matches a word up to vowel errors
            elif convert(query.lower()) in changed:
                ans.append(changed[convert(query.lower())][0])
            else:
                ans.append("")
        return ans


wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

wordlist = ["yellow"]
queries = ["YellOw"]

solution = Solution()
print(solution.spellchecker(wordlist, queries))

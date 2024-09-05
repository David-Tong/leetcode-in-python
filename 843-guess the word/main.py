import string


class Master(object):
    def __init__(self, secret, allowedGuesses):
        self.secret = secret
        self.allowedGuesses = allowedGuesses
        self.guesses = 0

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        self.guesses += 1
        if self.guesses > self.allowedGuesses:
            return -1

        guess = 0
        for x in range(len(word)):
            if self.secret[x] == word[x]:
                guess += 1
        return guess


class Solution(object):
    def findSecretWord(self, words, master):
        """
        :type words: List[Str]
        :type master: Master
        :rtype: None
        """
        M = 6
        N = len(words)

        # get hamming distance
        def getHamming(word, word2):
            hamming = 0
            for x in range(len(word)):
                if word[x] == word2[x]:
                    hamming += 1
            return M - hamming

        # pre-process
        from collections import defaultdict
        hammings = defaultdict(list)
        for word in words:
            for x in range(M + 1):
                hammings[word].append(set())
        for x in range(N):
            for y in range(x + 1, N):
                hamming = getHamming(words[x], words[y])
                hammings[words[x]][hamming].add(words[y])
                hammings[words[y]][hamming].add(words[x])

        # guess
        candidates = set(words)
        while len(candidates) > 0:
            for candidate in candidates:
                matched = master.guess(candidate)
                #if matched == -1:
                    #print("Either you took too many guesses, or you did not find the secret word.")
                candidates = candidates & hammings[candidate][M - matched]
                if len(candidates) == 0:
                    #print("You guessed the secret word correctly.")
                    return
                break


secret = "acckzz"
words = ["acckzz","ccbazz","eiowzz","abcczz"]
allowedGuesses = 10

secret = "hamada"
words = ["hamada","khaled"]
allowedGuesses = 10

secret = "azzzzz"
words = ["azzzzz","almnoz","abcdef","acdefg","adefgh","aefghi","afghij","aghijk","ahijkl","aijklm","ajklmn","aklmno","anopqr"]
allowedGuesses = 10

secret = "hbaczn"
words = ["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"]
allowedGuesses = 10

master = Master(secret, allowedGuesses)
solution = Solution()
print(solution.findSecretWord(words, master))

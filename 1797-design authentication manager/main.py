class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.time_to_live = timeToLive

        from collections import defaultdict
        self.tokens = defaultdict(str)

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.tokens[tokenId] = currentTime + self.time_to_live

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId in self.tokens:
            if self.tokens[tokenId] > currentTime:
                self.tokens[tokenId] = currentTime + self.time_to_live

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        for token in list(self.tokens):
            if self.tokens[token] <= currentTime:
                del self.tokens[token]
        return len(self.tokens)


am = AuthenticationManager(5)
am.renew("aaa", 1)
am.generate("aaa", 2)
print(am.countUnexpiredTokens(6))
am.generate("bbb", 7)
am.renew("aaa", 8)
am.renew("bbb", 10)
print(am.countUnexpiredTokens(15))

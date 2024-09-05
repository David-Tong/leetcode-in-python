class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = list()
        self.history.append(homepage)
        self.curr = 0
        self.limit = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.curr += 1
        self.limit = self.curr
        if len(self.history) <= self.limit:
            self.history.append(url)
        else:
            self.history[self.curr] = url

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.curr >= steps:
            self.curr -= steps
        else:
            self.curr = 0
        return self.history[self.curr]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.limit >= self.curr + steps:
            self.curr += steps
        else:
            self.curr = self.limit
        return self.history[self.curr]


"""
bh = BrowserHistory("leetcoce.com")
bh.visit("google.com")
bh.visit("facebook.com")
bh.visit("youtube.com")
print(bh.back(1))
print(bh.back(1))
print(bh.forward(1))
bh.visit("linkedin.com")
print(bh.forward(2))
print(bh.back(2))
print(bh.back(7))
"""

bh = BrowserHistory("leetcoce.com")
print(bh.forward(100))
print(bh.forward(50))
bh.visit("google.com")
bh.visit("facebook.com")
bh.visit("youtube.com")
print(bh.back(2))
bh.visit("apple.com")
print(bh.forward(1))
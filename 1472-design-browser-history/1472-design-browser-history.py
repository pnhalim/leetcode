class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = 0
        self.last = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.curr += 1
        self.last = self.curr
        if (self.curr == len(self.history)):
            self.history.append(url)
        else:
            self.history[self.curr] = url

    def back(self, steps: int) -> str:
        self.curr -= steps
        if self.curr < 0:
            self.curr = 0
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr += steps
        if (self.curr >= len(self.history) or self.curr > self.last):
            self.curr = min(len(self.history) - 1, self.last)
        return self.history[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
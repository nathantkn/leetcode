class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.currPage = 0
        self.length = 0

    def visit(self, url: str) -> None:
        self.currPage += 1
        if self.currPage == len(self.stack):
            self.stack.append(url)
        else:
            self.stack[self.currPage] = url
        self.length = self.currPage

    def back(self, steps: int) -> str:
        self.currPage = max(0, self.currPage - steps)
        return self.stack[self.currPage]

    def forward(self, steps: int) -> str:
        self.currPage = min(self.currPage + steps, self.length)
        return self.stack[self.currPage]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

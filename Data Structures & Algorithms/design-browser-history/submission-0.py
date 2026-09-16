class LinkedListNode:
    def __init__(self, val = "", prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.tail = self.current = LinkedListNode(homepage)

    def visit(self, url: str) -> None:
        new_url = LinkedListNode(url, self.current)
                
        self.current.next = new_url
        self.current = self.tail = new_url

    def back(self, steps: int) -> str:
        while self.current != self.head:
            if steps == 0:
                break
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while self.current != self.tail:
            if steps == 0:
                break
            self.current = self.current.next
            steps -= 1

        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
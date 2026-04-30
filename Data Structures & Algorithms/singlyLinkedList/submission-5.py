class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = self.tail = LinkedListNode(-1)
    
    def get(self, index: int) -> int:
        curr, i = self.head.next, 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = LinkedListNode(val, self.head.next)
        self.head.next = newNode
        if not newNode.next: # list was empty before insertion
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = LinkedListNode(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            curr = curr.next
            i += 1

        # curr is the node before index and curr.next is the index to remove
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values

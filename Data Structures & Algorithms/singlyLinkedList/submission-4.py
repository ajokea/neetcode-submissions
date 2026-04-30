class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = self.tail = None
    
    def get(self, index: int) -> int:
        curr, i = self.head, 0
        while curr:
            if i == index:
                break
            curr = curr.next
            i += 1
        return curr.val if curr else -1

    def insertHead(self, val: int) -> None:
        newNode = LinkedListNode(val)
        if not self.head:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertTail(self, val: int) -> None:
        newNode = LinkedListNode(val)
        if not self.tail:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def remove(self, index: int) -> bool:
        i = 0
        prev, curr = None, self.head
        while curr:
            if i == index:
                break

            prev, curr = curr, curr.next
            i += 1

        if i < index or not curr:
            return False
        else:
            if curr == self.head:
                if self.tail == self.head:
                    self.tail = self.tail.next
                self.head = self.head.next
            else:
                prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
            
            return True


    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values

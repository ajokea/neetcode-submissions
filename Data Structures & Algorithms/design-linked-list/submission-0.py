class LinkedListNode:
    
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = self.tail = None

    def get(self, index: int) -> int:
        current = self.head
        for i in range(index):
            if not current:
                break
            current = current.next

        return current.val if current else -1

    def addAtHead(self, val: int) -> None:
        new_head = LinkedListNode(val)
        if self.head:
            new_head.next = self.head
        else:
            self.tail = new_head
        self.head = new_head

    def addAtTail(self, val: int) -> None:
        new_tail = LinkedListNode(val)
        if self.tail:
            self.tail.next = new_tail
        else:
            self.head = new_tail
        self.tail = new_tail

    def addAtIndex(self, index: int, val: int) -> None:
        i, prev, current = 0, None, self.head
        while current:
            if i == index:
                break
            prev = current
            current = current.next
            i += 1

        if i == index:
            if current == self.head: # index = 0
                self.addAtHead(val)
            elif prev == self.tail: # index = length of list
                self.addAtTail(val)
            else:
                new_node = LinkedListNode(val)
                prev.next = new_node
                new_node.next = current

    def deleteAtIndex(self, index: int) -> None:
        i, prev, current = 0, None, self.head
        while current:
            if i == index:
                break
            prev = current
            current = current.next
            i += 1

        if i == index and current:
            if current == self.head:
                self.head = self.head.next
            elif current == self.tail:
                self.tail = prev
                prev.next = None
            else:
                prev.next = current.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
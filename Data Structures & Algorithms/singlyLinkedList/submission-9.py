class Node:
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = self.tail = None
    
    def get(self, index: int) -> int:
        i, current = 0, self.head

        while current:
            if i == index:
                return current.val
            current = current.next
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head)
        if not self.head:
            self.tail = node
        self.head = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if not self.tail:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        i, prev, current = 0, None, self.head
        while current and i < index:
            prev = current
            current = current.next
            i += 1

        # out of bounds
        if not current:
            return False
        # head
        elif current == self.head:
            # only one node
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
        else:
            prev.next = current.next
            if current == self.tail:
                self.tail = prev
        return True       

    def getValues(self) -> List[int]:
        values = []
        current = self.head
        while current:
            values.append(current.val)
            current = current.next
        return values

class MyNode:
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next

class MyQueue:
    def __init__(self, items = []):
        self.head = self.tail = None
        self.size = 0
        for item in items:
            self.enqueue(item)

    def enqueue(self, val):
        new_node = MyNode(val)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        node = self.head
        self.head = self.head.next
        node.next = None
        self.size -= 1
        return node

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_q = MyQueue(students)
        sandwich_q = MyQueue(sandwiches)

        count = 0
        while count != student_q.size:
            student = student_q.dequeue()

            if student.val == sandwich_q.head.val:
                sandwich_q.dequeue()
                count = 0
            else:
                student_q.enqueue(student.val)
                count += 1

        return count
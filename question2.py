import delete_operation_singly_linkedlist as linkedList

class stack:
    def __init__(self):
        self.list = linkedList.SinglyLinkedList()

    def push(self, data):
        self.list.append(data)

    def pop(self):
        self.top()
        self.list.delete_last_node()

    def top(self):
        current = self.list.head
        while current.next != None:
            current = current.next
        return current

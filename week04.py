class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if None == self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)

    def __str__(self):
        txt = ""
        node = self.head
        while node:
            txt += f"{node.data} -> "
            node = node.link
        return txt + "end"

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
# a = Node("d")
# print(a.data)
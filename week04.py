import random


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

    def search(self, target):
        current = self.head
        while current.link:
            if current.data == target:
                return f"{target}을(를) 찾았습니다."
            else:
                current = current.link
        return f"{target}은(는) 리스트 안에 존재하지 않습니다."

    def __str__(self):
        txt = ""
        node = self.head
        while node:
            txt += f"{node.data} -> "
            node = node.link
        return txt + "end"

ll = LinkedList()
for _ in range(20):
    ll.append(j := random.randint(1, 30))
    print(j, end=" ")
print(ll.search(10))


# ll.append(8)
# ll.append(10)
# ll.append(-9)
# print(ll)
# print(ll.search(99))
# print(ll.search(-9))
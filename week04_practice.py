class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    # 이 메소드는 O(n)선형시간이 소요되는데..?
    def append(self, data):
        if None == self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link #이 코드는 가장 마지막에만 추가하네.
        current.link = Node(data)
        return

    def remove(self, target):
        if self.head.data == target:
            self.head = self.head.link
            return

        current = self.head
        next_node = self.head.link
        while next_node:
            if next_node.data == target:
                current.link = next_node.link
                next_node.link = None
                return
            current = next_node
            next_node = next_node.link

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return f"{target}을(를) 찾았습니다."
            else:
                current = current.link
        return f"{target}은(는) LinkedList 안에 존재하지 않습니다."

    def __str__(self):
        node = self.head
        txt = ""
        while node:
            txt += f"{node.data} -> "
            node = node.link
        return txt + "end"

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
print(ll.search(100))
print(ll.search(10))
ll.remove(90)
ll.remove(10)
print(ll)
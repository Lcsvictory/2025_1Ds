class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 이 메소드는 O(n)선형시간이 소요되는데..?
    def append(self, data):
        node = Node(data)
        if None == self.head:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.link = node
            self.tail = node
            return
        # current = self.head
        # while current.link:
        #     current = current.link #이 코드는 가장 마지막에만 추가하네.
        
        

    def remove(self, target):
        current = self.head
        if self.head.data == target:
            self.head = self.head.link
            current.link = None
            return

        # current = self.head
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
    
    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            temp = current.link
            current.link = previous
            previous = current
            current = temp
        self.head = previous
            

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
# ll.reverse_list()
# print(ll)
# ll.reverse_list()
# print(ll)
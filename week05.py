class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.link = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return "stack is empty"
        popped_node = self.top
        self.top = self.top.link
        popped_node.link = None
        return popped_node.data

    def peek(self):
        if self.top is None:
            return ""
        print(self.top.data)

    def size(self):
        current = self.top
        cnt = 0
        if self.top is None:
            return 0
        while current:
            cnt += 1
            current = current.link
        return cnt

    def is_empty(self):
        if self.top is None:
            return True
        return False

s1 = Stack()
s1.push("data structure")
s1.peek()
s1.push("database")
s1.push("database")

s1.push("database")

s1.push("databaseasdsd")
print(s1.size())
s1.peek()
s1.pop()

s1.pop()
# s1.pop()
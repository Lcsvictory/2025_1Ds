from queue import Queue


class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class made_Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self,data):
        self.size += 1
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node # 여기서 link는 진짜 rear가 아니네.
            self.rear = node # 이게 진짜 rear. 따라서 rear.link는 무조건 None

    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
            # raise IndexError("queue is empty")
            return
        self.size -= 1
        temp = self.front
        self.front = temp.link
        temp.link = None
        if self.front is None:
            self.rear = None
        return temp.data

q = made_Queue()
q.enqueue("ds")
q.enqueue("DB")
# q.enqueue("하이")
print(q.size, q.front.data, q.rear.data, q.rear.link)

print(q.dequeue())
print(q.size, q.front.data, q.rear.data, q.rear.link)

print("=======================")
qq = Queue()
qq.put("ds")
qq.put("DB")
qq.put("hello")
print(qq.__dir__())
print(qq.qsize())

print(qq.get())
print(qq.qsize())

print(qq.get())
print(qq.qsize())


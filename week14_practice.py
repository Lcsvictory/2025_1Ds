import sys

sys.setrecursionlimit(10 ** 9)
class ThreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def post_order1(node):
    if node is None : return

    stack = list()
    output = list()
    stack.append(node)

    while stack:
        current = stack.pop()
        output.append(current.data)

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    for v in reversed(output):
        print(v)
def insert(root :ThreeNode, val :int):
    if root is None: return

    temp = ThreeNode(val)

    current = root
    while True:
        if current.data > temp.data:
            if current.left is None:
                current.left = temp
                return
            current = current.left
        else :
            if current.right is None:
                current.right = temp
                return
            current = current.right


if __name__ == "__main__" :
    inputs = sys.stdin.readline
    temp = []
    while True:
        try:
            user_input = int(inputs().strip())
            temp.append(user_input)
        except:
            break

    root = ThreeNode(temp[0])
    for i in temp[1:]:
        insert(root, i)
    post_order1(root)






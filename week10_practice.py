class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def pre_order(node):
    if node is None:
        return
    print(node.data, end='->')
    pre_order(node.left)
    pre_order(node.right)

def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end='->')
    in_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end='->')

def insert(node, value) -> None:
    nNode = TreeNode()
    nNode.data = value

    if node is None:
        node = nNode
        return

    current = node
    while True:
        if value < current.data:
            if current.left is None:
                current.left = nNode
                break
            current = current.left
        else:
            if current.right is None:
                current.right = nNode
                break
            current = current.right
    return


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 14]
    # numbers = [10, 15, 8, 3, 9, 1, 7, 100]
    root = TreeNode()
    root.data = numbers[0]

    for number in numbers[1:]:
        insert(root, number)

    post_order(root)  # 3->9->8->15->10
    print()
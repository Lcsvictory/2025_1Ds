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
        
def search(node, value):
    if node is None:
        return False
    current = node
    if current.data == value:
        return True
    elif current.data > value:
        return search(current.left, value)
    else:
        return search(current.right, value)

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


def delete(node, value):
    if node is None:
        print("노드가 비어있습니다. or 삭제할 값이 없습니다.")
        return None
    if value < node.data:
        node.left = delete(node.left, value)
    elif value > node.data:
        node.right = delete(node.right, value)
    else:  # 삭제할 값을 가지고 있는 노드를 찾음
        # leaf노드인 경우....
        if node.left is None and node.right is None:
            return None
        # 자식 노드가 1개인 경우
        elif node.left is None or node.right is None:
            return node.right if node.left is None else node.left
        # 자식 노드가 2개인 경우...
        right_tree_min_node = node.right
        while right_tree_min_node.left:
            right_tree_min_node = right_tree_min_node.left
        node.data = right_tree_min_node.data
        node.right = delete(node.right, right_tree_min_node.data)
    return node

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 14]
    # numbers = [10, 15, 8, 3, 9, 1, 7, 100]
    root = TreeNode()
    root.data = numbers[0]

    for number in numbers[1:]:
        insert(root, number)

    post_order(root)  # 3->9->8->15->10
    print()
    if search(root, 7):
        print("찾았다")
    else:
        print("못 찾았다.")
        
    root = delete(root, 10)
    post_order(root)
    print()
    in_order(root)
    print()
    pre_order(root)
    print()
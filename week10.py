
class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end=" -> ")
    in_order(node.right)



def pre_order(node):
    if node is None:
        return
    print(node.data, end=" -> ")
    pre_order(node.left)
    pre_order(node.right)


def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end=" -> ")


def search(find_number) -> bool:
    current = root
    while True:
        if find_number == current.data:
            return True
        elif find_number < current.data:
            if current.left is None:
                return False
            current = current.left
        else:
            if current.right is None:
                return False
            current = current.right

#함수의 파라미터는 참조하지 않는가?
def insert(root, *, value):
    node = TreeNode()
    node.data = value

    if root is None:
        return node

    current = root

    while True:
        if node.data < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right
    return root

def delete(node, value):
    if node is None:
        print("노드가 비어있습니다. or 삭제할 값이 없습니다.")
        return None
    if value < node.data:
        node.left = delete(node.left, value)
    elif value > node.data:
        node.right = delete(node.right, value)
    else: #삭제할 값을 가지고 있는 노드를 찾음
        #leaf노드 이거나 자식이 1개인 경우....
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        #자식 노드가 2개인 경우...
        #right 트리에서 가장 작은 노드를 찾자.
        #right_tree_min_num = node.right
        #while right_tree_min_num.left:
        #    right_tree_min_num = right_tree_min_num.left
        #node.data = right_tree_min_num.data
        #node.right = delete(node.right, right_tree_min_num.data)

        #left 트리에서 가장 큰 노드를 찾자.
        left_tree_max_num = node.left
        while left_tree_max_num.right:
            left_tree_max_num = left_tree_max_num.right
        node.data = left_tree_max_num.data
        node.left = delete(node.left, left_tree_max_num.data)
    return node




if __name__ == "__main__":
    numbers = [10,15,8,3,9, 100, 7, 13]

    #리턴값으로 참조를 계속 업데이트함. return값이 없으면 None을 반환하니
    # root참조가 None으로 변경되버림

    #root = None
    #for number in numbers:
        #root = insert(root=root, value=number)

    # 파이썬은 참조니까.
    root = TreeNode()
    root.data = numbers[0]
    for number in numbers[1:]:
        insert(root=root, value=number)

    print("binarySearchTree 구성완료")
    #find_number()
    post_order(root)
    print()
    in_order(root)
    print()
    pre_order(root)
    print()
    #find_num = int(input("찾을 숫자를 입력 : "))
    find_num = 13
    if search(find_num):
        print(f"{find_num}을(를) 찾았습니다")
    else:
        print(f"{find_num}이(가) 존재하지 않습니다.")


    delete_num = int(input("삭제할 숫자를 입력 : "))
    #delete(root,delete_num)
    root = delete(root, delete_num)
    post_order(root)
    print()
    in_order(root)
    print()
    pre_order(root)
    print()
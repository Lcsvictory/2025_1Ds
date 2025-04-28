

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


def find_number():
	find_number = int(input("찾을 숫자를 입력 : "))
	current = root
	while True:
		if find_number == current.data:
			print(f"{find_number}을(를) 찾았습니다")
			break
		elif find_number < current.data:
			if current.left is None:
				print(f"{find_number}이(가) 존재하지 않습니다")
				break
			current = current.left
		else:
			if current.right is None:
				print(f"{find_number}이(가) 존재하지 않습니다")
				break
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

class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None



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


import random
import time

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

class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None



if __name__ == "__main__":
	first = time.time()
	print(first)
	numbers = [random.choice(range(1,101)) for _ in range(100)]
	#numbers = [i for i in range(1, 101)]
	#numbers = [10,15,8,3,9]
	root = None

	node = TreeNode()
	node.data = numbers[0]
	root = node

	for number in numbers[1:]:
		node = TreeNode()
		node.data = number
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

	print("binarySearchTree 구성완료")
	last = time.time()
	print("소요시간 : " + str(last-first))
	#find_number()
	in_order(root)



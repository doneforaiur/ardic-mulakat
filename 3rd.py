class Node: 
	def __init__(self):
		self.left = None
		self.right = None

def duplicate_detection(root):
	current = root
	stack = []
	nodes = []

	while True:
		if current is not None:
			if current in nodes:
				return True
			nodes.append(current)
			stack.append(current)
			current = current.left
		elif(stack):
			current = stack.pop()
			current = current.right
		else:
			break
	return False
			
if __name__ == '__main__':
	root = Node()
	root.left = root
	
	faulty_link = Node()
	
	root.right = faulty_link
	root.right.left = faulty_link
	
	print(duplicate_detection(root))

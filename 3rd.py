class Node:
    def __init__(self):
        self.left = None
        self.right = None
	
def inorderTraversal(root):
	current = root
	stack = []
	res = []
	
	while True:
		if current is not None:
			stack.append(current)
			current = current.left
		elif(stack):
			current = stack.pop()
			res.append(current)
			current = current.right
		else:
			break
	
	return res


def check_collision(root):
	nodes = inorderTraversal(root)
	check = any(nodes.count(node) > 1 for node in nodes)
	return check

if __name__ == '__main__':
	root = Node()
	
	faulty_link = Node()
	
	root.left  = Node()
	root.right = Node()
	
	root.left.right = faulty_link
	#root.left.right = Node()
	root.right.left = faulty_link
	

	print(check_collision(root))

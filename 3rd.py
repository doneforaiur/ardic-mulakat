class Node:
    def __init__(self):
        self.left = None
        self.right = None
		
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root)
            res = res + self.inorderTraversal(root.right)
        return res

def check_collision(root):
	nodes = root.inorderTraversal(root)
	check = any(nodes.count(node) > 1 for node in nodes)
	return check

if __name__ == '__main__':
	root = Node()
	
	faulty_link = Node()
	
	root.left  = Node()
	root.right = Node()
	
	#root.left.right = faulty_link
	root.left.right = Node()
	root.right.left = faulty_link
	

	print(check_collision(root))

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

# problem; checks whole tree
def check_collision(root1, root2):
	nodes1 = root1.inorderTraversal(root1)
	nodes2 = root2.inorderTraversal(root2)

	check = any(node in nodes1 for node in nodes2)
	return check


if __name__ == '__main__':

	root2 = Node()
	root1 = Node()

	faulty_link = Node()

	root1.left = faulty_link
	root1.right = Node()

	root2.left = faulty_link
	root2.right = Node()

	print(check_collision(root1, root2))

class newNode: 
	def __init__(self):
		self.left = None
		self.right = None
 
# problem; recursion 
def checkDupUtil(root, nodes) :
    if (root == None) :
        return False
		
    if root in nodes: 
        return True
  
    nodes.add(root) 
	
    return checkDupUtil(root.left, nodes) or checkDupUtil(root.right, nodes) 
 
def checkDup(root):
    nodes=set() 
    return checkDupUtil(root, nodes) 
  

if __name__ == '__main__':
	root = newNode() 
	root.right = root

	faulty_link = newNode()

	root.left = faulty_link
	root.left.left = faulty_link 
	if (checkDup(root)):
		print("Yes")
	else:
		print("No")
  

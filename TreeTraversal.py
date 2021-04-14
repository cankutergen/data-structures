# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

   
def inorder(root, arr):
  if root:
    inorder(root.left, arr)
    arr.append(root.val)
    inorder(root.right, arr)
        
def preorder(root, arr):
  if root:
    arr.append(root.val)
    inorder(root.left, arr)     
    inorder(root.right, arr)
    
import queue
def levelOrder(root):
    arr = []
    q = queue.Queue()

    if root:
        q.put(root)

    while not q.empty():
        level = []

        for _ in range(q.qsize()):             
            node = q.get()
            level.append(node.val)

            if node.left is not None:
                q.put(node.left)

            if node.right is not None:
                q.put(node.right)

        arr.append(level)

    return arr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__ (self):
        self.maxD =1
        self.currentDepth=1
        
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if root ==None:
            return(0)
        if root.left==None and root.right==None:
            return(max(self.maxD,self.currentDepth))
        if root.left!=None:
            self.currentDepth+=1
            self.maxD=self.maxDepth(root.left)
            self.currentDepth-=1
        if root.right!=None:
            self.currentDepth+=1
            self.maxD=self.maxDepth(root.right)
            self.currentDepth-=1
        return(self.maxD)
    
    def maxDepth(self, root):
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 

        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return(None)
        if root.val == val:
            return(root)
        if root.left==None and root.right==None:
            return(None)
        result=self.searchBST(root.left,val)
        if result != None:
            return(result)
        result=self.searchBST(root.right,val)
        if result != None:
            return(result)   
        return None
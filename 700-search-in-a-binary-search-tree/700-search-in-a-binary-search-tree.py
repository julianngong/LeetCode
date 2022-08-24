# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if (root==None or val == root.val):
            return(root)
        if val<root.val:
            return(self.searchBST(root.left,val)) #note with recursion as soon as something is returned like this in a tree it is returned all the way up
        else:
            return(self.searchBST(root.right,val))

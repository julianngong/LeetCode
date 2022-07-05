"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        queue =  [root]
        while queue:
            elemsinrow = len(queue)
            for i in range(elemsinrow):
                node = queue.pop(0)
                if i<elemsinrow-1:
                    node.next = queue[0]
                else:
                    node.next = None
                if (node.left != None) and (node.right!= None):
                    queue.append(node.left)
                    queue.append(node.right)
        return(root)
            
        
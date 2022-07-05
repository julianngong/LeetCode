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
        if root == None: #if the tree is empty then just return the tree
            return root
        queue =  [root] #make the first element of the queue the root
        while queue: # while the queue is not empty
            elemsinrow = len(queue) # note each bfs loop we will add the number of children to the queue so the current length of the queue during the iteration is the number of elements in the row
            for i in range(elemsinrow):  # for all the nodes in the row
                node = queue.pop(0) #get the first element of the queue
                if i<elemsinrow-1: # if its not the last element of the row 
                    node.next = queue[0]#connect it to the next element coming up in the queue
                else:
                    node.next = None #else assign to none
                if (node.left != None) and (node.right!= None): # if its not a leaf of the graph
                    queue.append(node.left) # add the left node to the queue
                    queue.append(node.right) # add the right node to the queue
        return(root)
            
        
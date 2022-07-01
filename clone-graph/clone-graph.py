"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = {} #need a hash map to act like a set of unique values
        queue = deque([node]) #make a queue and add the first node to the queue
        visited[node] = Node(node.val, []) #this visited hash map used the old node as the key and the duplicated node as its value. initislly we say ti has no connecting nodes as we dunno what they are yet
        while queue: 
            currentnode = queue.popleft() #while the queue isnt empty pop the node at the bottom of the queue
            for neighbor in currentnode.neighbors: #for each of this current nodes neigbours
                if neighbor not in visited: # if the node its pointing to is not in visited then it has not been seen or duplicated yet
                    newnode = Node(neighbor.val,[]) #make a new object with the same vakue but empty neighbours list as we dunno what they will be yet and they need to be new objects
                    queue.append(neighbor) #add this neighbor to the lsit
                    visited[neighbor]=newnode #set the duplicate of the new node to the hash of the old node
                visited[currentnode].neighbors.append(visited[neighbor])#add the copy node to the list of nodes for the current node
        return visited[node]

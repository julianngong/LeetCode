class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        listzero = [0]
        queue = collections.deque() #make an empty queue
        queue.append(listzero) #add the list of 0 to the queue which represents the current paths
        seen = set(tuple([0])) #add each current path to the seen set not just the node
        paths = [] 
        while queue: #while the stack is not empty, not although using queue data type we only take elements from the front and add to the back so its a stack
            currentpath = queue.popleft() #get the bottom element of the stack and remove from stack
            currentnode = currentpath[-1] #get the most recently reached node from the most current path
            if currentnode == n-1: #if the most recently reached node is the wanted node then add this path to the list of valid paths
                paths.append(currentpath)
            for neighbours in graph[currentnode]: #for the most recently reached node check all its neighbours.
                newpath = currentpath+[neighbours] #add each to the current path to make a new path
                if tuple(newpath) not in seen: #now want to check if we have checked this path yet or not.
                    seen.add(tuple(newpath))#if not then add to the list of seen paths
                    queue.append(newpath)#add this path to the queue of the paths to check further
        return(paths)
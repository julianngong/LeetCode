class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def BFS(start,target,graph):
            currentproduct = 1.0 #each node should start with a value of 1 as dividing something by itself gets 1
            queue = collections.deque([(start, currentproduct)]) # make a queue for BFS where each element is a tuple with the name of the node and its current product value
            visited = set()
            while queue: # while the queue is not empty
                front,currentproduct = queue.popleft() # get the first node in the queue
                if front == target: # if this node is the wanted node then return the current product
                    return(currentproduct)
                visited.add(front) # if the node is not the wanted node then add this node to visited
                for neighbour,value in graph[front]: # for every neighbour of this front node
                    if neighbour not in visited: # if we havnt seen one of the neighbours nodes yet add it to queue
                        queue.append((neighbour,value*currentproduct)) # the queue will contain the neighbour node and the current product. not if you want to keep track of the elements which had to be traversed, instead of doing value*product in the tuple, make this other element a list of currently traversed nodes so do currentnodes.append(neighbour)
            return(-1.0)
        
        graph = {} # make a new graph
        for equation,val in zip(equations,values): # want each equations to be paired with each value and for each of these pairs in the list
            top,bottom = equation # sets top and bottom to the first and second value of the equation list
            if top in graph: # if this node is already in the graph
                graph[top].append((bottom,val)) # append
            else: # if its not already in the graph then add a new list 
                graph[top] = [(bottom,val)]
            if bottom in graph:
                graph[bottom].append((top,1/val))
            else:
                graph[bottom] = [(top,1/val)]
        print(graph)
        result = []
        for query in queries: #for each of the possible queries
            start,target = query
            if start not in graph or target not in graph:
                result.append(-1.0)
            else:
                result.append(BFS(start,target,graph)) # run bfs on these two pairs
        return(result)
            
            

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
        if destination in graph.keys(): # if the end node points to any elemnents then automatically return false
            return False
        stack = [source]
        visited = [0 for _ in range(n)] #we need to determine if its the vist time its been visited in the selected path 0, its been visted before in thios path 1 or we already know we can make it to the destination node from a path on this node 2
        while stack:
            current = stack[-1] #get the first element but dont pop from stack yet
            visited[current] = 1 # set this element as just visited for first time in this path
            for neighbours in graph[current]: # for all neighbours of this node
                if visited[neighbours] ==1: #if a neighbour is labelled one then it has been visited before on this path hence we would be forming a loop so return false
                    return(False)
                elif visited[neighbours] == 0: # if this neighbour has never been v isited before then add it to the stack of nodes to check next
                    stack.append(neighbours)
                #note if visited is 2 then we can ignore and do nothing and just remove this node from the stack
            if current == stack[-1]:
                if (len(graph[current]) == 0) and (current != destination):
                    return(False)
                else:
                    visited[stack.pop()] =2
        return(True)
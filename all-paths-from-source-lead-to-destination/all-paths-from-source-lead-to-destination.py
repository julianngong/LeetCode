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
                #note if visited is 2 then we can ignore and do nothing as it will lead to the destination node
            if current == stack[-1]: #if nothing has been added to the stack aka all the neighbours are 2 or it had no neighbours in the first place. if something has been added then go down that path
                if (len(graph[current]) == 0) and (current != destination): #if it had no neighbours and the node is not equal to the destination then return false
                    return(False)
                else: #else just pop this node and move on as it will either have a neghour point to a 2 meaning it will lead to destination node or it is the destinatio node so again set it as 2.
                    visited[stack.pop()] =2
        return(True)
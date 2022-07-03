class Solution: #This entire bit is based on finding a path ensuring all edges are visited at least once but nodes can be visited any number of times
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for x,y in sorted(tickets)[::-1]: #this [::-1] means the list backwards, so this is done here to make sure the reversed order is correct without hjaving to use parameters in sorted function
            graph[x].append(y) #all this just turns our list of edges into a graph adgecency list
        route = [] 
        stack = ['JFK']
        while stack:
            while graph[stack[-1]]: #while the current top of the stack has connecting edges
                stack.append(graph[stack[-1]].pop()) #add in order each of the nodes connecting to expore down. this removes the edge from the graph so when this node is visited again it will be empty if it only had one edge. hence it will be added to the stack on backtrack
            route.append(stack.pop()) #the first time a node is a dead end aka all outgoing edges have been explored add it to the route
        return route[::-1] #we then want to go along this route backwards to get the final answer
#`All in all the method is as followed. first order the starting node alphabetically and go to the first connecting node. repeat and go to this first connecting node (popping this connecting node form the graph) until we get to a node which we have visited all its outgoing edges. we know this by popping the edge of that node from the graph as soon as we traverse down it. once this node is found with no edges add it to the route aka exit the while loop and append it. then backtrack to the previous node and explore all their edges. this backtrack happens automatically from now popping the top element of stack and looking at those edges. repeat this until stack is empty then return the route stack in reverse order.
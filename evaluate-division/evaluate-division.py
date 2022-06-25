class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def BFS(start,target,graph):
            currentproduct = 1.0
            queue = collections.deque([(start, currentproduct)])
            visited = set()
            while queue:
                front,currentproduct = queue.popleft()
                if front == target:
                    return(currentproduct)
                visited.add(front)
                for neighbour,value in graph[front]:
                    if neighbour not in visited:
                        queue.append((neighbour,value*currentproduct))
            return(-1.0)
        graph = {}
        for equation,val in zip(equations,values):
            top,bottom = equation
            if top in graph:
                graph[top].append((bottom,val))
            else:
                graph[top] = [(bottom,val)]
            if bottom in graph:
                graph[bottom].append((top,1/val))
            else:
                graph[bottom] = [(top,1/val)]
        print(graph)
        result = []
        for query in queries:
            start,target = query
            if start not in graph or target not in graph:
                result.append(-1.0)
            else:
                result.append(BFS(start,target,graph))
        return(result)
            
            
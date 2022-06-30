class Solution:  
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2) #connect edges and make graph with all edges
            neighbors[n2].append(n1)

        queue = collections.deque([source])
        seen = set([source])

        while queue:
            # Get the current node.
            node = queue.popleft()

            # Check if we have reached the target node.
            if node == destination:
                return True

            # Add all neighbors to the queue.
            for neighbor in neighbors[node]:
                # Check if neighbor has been added to the queue before.
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        # Our queue is empty and we did not reach the end node.
        return False
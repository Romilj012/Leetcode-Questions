class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        start_node = None
        for node in graph:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break
        if start_node is None:  # If no imbalance, start from any node with outgoing edges
            start_node = next(iter(graph))
        stack = [start_node]
        path = []
        
        while stack:
            while graph[stack[-1]]:
                next_node = graph[stack[-1]].popleft()
                stack.append(next_node)
            path.append(stack.pop())
        path.reverse()
        result = [[path[i], path[i + 1]] for i in range(len(path) - 1)]
        return result

    

        
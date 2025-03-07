from collections import deque
def bfs(graph,start):
    visited =set()
    queue=deque()
    order=[]

    visited.add(start)
    queue.append(start)
    while queue:
        current=queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                order.append(neighbor)
    
    return order

graph={
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

result=bfs(graph,'A')
print('here is the result of bfs: ',result)

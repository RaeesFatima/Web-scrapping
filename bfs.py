from collections import deque

def bfss(graph, start):
    visited=set()
    queue=deque()

    queue.append(start)
    visited.add(start)

    order=[]
    while queue:
        current=queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return order
    
graph={
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

result=bfss(graph,'A')
print('here is the result of bfs: ',result)
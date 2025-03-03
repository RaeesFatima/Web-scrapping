from collections import deque

def bfs(graph,start):
    queue=deque()
    visited=set()

    order=[]

    queue.append(start)
    visited.add(start)

    while queue:
        current=queue.popleft()
        order.append(current)

        for neighbors in graph[current]:
            if neighbors not in visited:
                queue.append(neighbors)
                visited.add(neighbors) 

    return order

graph = {
    '0': ['1', '2'],
    '1': ['3', '4'],
    '2': ['5', '6'],
    '3': [],
    '4': ['7'],
    '5': [],
    '6': [],
    '7': []
}


result=bfs(graph,'0')
print('here is the result of bfs: ',result)
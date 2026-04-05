def bfs(start, goal):
    q = [start]
    visited = []
    while q:
        y = q.pop(0)
        if y == goal: 
            visited.append(y)
            print(visited)
            return
        visited.append(y)
        q.extend(graph[y])
        
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "M"],
    "G": ["N", "O"],
    "H": [],
    "I": [],
    "J": [],
    "K": [],
    "L": [],
    "M": [],
    "N": [],
    "O": []
}
bfs("A","O")
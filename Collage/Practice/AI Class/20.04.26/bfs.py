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
            q.extend(g[y])

g = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["F","G"],
    "D":["H","I"],
    "E":["J"],
    "F":[],
    "G":[],
    "H":[],
    "I":[],
    "J":[]
}
bfs("A", "J")
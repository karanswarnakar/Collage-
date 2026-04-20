def dfs(start, goal):
    q = [start]
    visited = []
    while q:
        y = q.pop()
        if y==goal:
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
dfs("A", "J")
def dfs(start,goal):
    q = [start]
    visited = []
    
    while q:
        y = q.pop()
        visited.append(y)
        
        if y == goal: 
            print(visited)
            return
        
        q.extend(graph[y])
graph = {
    "A":["B", "C"],
    "B":["D"],
    "C":["E", "F", "G"],
    "D":[],
    "E":[],
    "F":[],
    "G":[],
} 


dfs("A","G")
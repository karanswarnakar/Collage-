def bestfs(start,goal):
    q = [start]
    visited  = []
    
    while q:
            q.sort(key=lambda x: h[x])
            y = q.pop()
            visited.append(y) 
            
            if y==goal:
                print(visited)
                return
            for i in graph[y]:
                if i not in q and i not in visited:
                    q.append(i)

graph = {
    "A":["B", "C"],
    "B":["D"],
    "C":["E", "F", "G"],
    "D":[],
    "E":[],
    "F":[],
    "G":[],
} 
h = {
    "A":0,
    "B":5,
    "C":3,
    "D":2,
    "E":8,
    "F":9,
    "G":1,
}            


bestfs("A", "G")            
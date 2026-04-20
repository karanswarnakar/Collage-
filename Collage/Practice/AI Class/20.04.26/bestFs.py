
def bestFs(start,goal):
    q = [start]
    visited = []
    
    while(q):
        q.sort(key=lambda x: h[x])
        y = q.pop(0)
        visited.append(y)
        
        if y==goal:
            print(visited)
            return
        for i in g[y]:
            if i not in q and i not in visited:
                q.append(i)
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
h = {
    "A":0,
    "B":5,
    "C":2,
    "D":4,
    "E":3,
    "F":2,
    "G":8,
    "H":6,
    "I":7,
    "J":1
}

bestFs("A","J")
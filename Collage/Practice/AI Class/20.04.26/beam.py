def beam_search(start, goal, width):
        q = [start]
        visited = []
        
        while(q):
            new = []
            for y in q:
                visited.append(y)
                
                if y == goal:
                    print(visited)
                    return

                for i in graph[y]:
                    if i not in q and i not in visited:
                        new.append(i)
                new.sort(key=lambda x: h[x])
                q = new[:width]
graph = {
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

beam_search("A","J",2)
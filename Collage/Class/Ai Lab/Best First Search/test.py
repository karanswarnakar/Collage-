# graph = {
#     "A":["B","C"],
#     "B":["D","E"]
# }

# print(graph["B"])

# h = {"A":0, "B":3, "C":2}

# print(h["C"])

# q = ["A"]
# q.append("B")
# q.append("C")

# print(q)

# def bestfs(start, goal):
#     q = [start]
#     visited = []
    
#     while(q):
#         q.sort(key=lambda x: h[x])
#         y = q.pop(0)
        
#         visited.append(y)  
        
#         if y == goal:
#             print(visited)
#             return
        
#         for i in graph[y]:
#             if i not in q and i not in visited:
#                 q.append(i)
# graph = {
#     "A":["B","C"],
#     "B":["D","E"],
#     "C":["F","G"],
#     "D":[],
#     "E":[],
#     "F":[],
#     "G":[]
# }
# h = {
#     "A":0,
#     "B":5,
#     "C":2,
#     "D":9,
#     "E":7,
#     "F":6,
#     "G":1
# }
     
# bestfs("A", "G")


# q = ["B"]
# newSort = ["B","F","G"]
# visited = ["A","C"]

# q = newSort[:2]
# print(q) 
def bestfs(start, goal):
    q = [start]
    visited = []
    
    while(q):
        q.sort(key=lambda x: h[x])
        y = q.pop(0)
        
        visited.append(y)  
        
        if y == goal:
            print(visited)
            return
        
        for i in graph[y]:
            if i not in q and i not in visited:
                q.append(i)
graph = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["F","G"],
    "D":["H"],
    "E":["I"],
    "F":["J"],
    "G":["K","L"],
    "H":[],
    "I":[],
    "J":[],
    "K":[],
    "L":[]
}
h = {
    "A":0,
    "B":3,
    "C":2,
    "D":5,
    "E":3,
    "F":9,
    "G":6,
    "H":1,
    "I":99,
    "J":99,
    "K":99,
    "L":3
}   
bestfs("A", "H")
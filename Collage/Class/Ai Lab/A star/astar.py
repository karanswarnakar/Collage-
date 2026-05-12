def a_star(start, goal):
    open_list = [(start, 0, [start])]

    while open_list:
        current, g, path = min(open_list, key=lambda x: x[1] + h[x[0]])
        open_list.remove((current, g, path))

        if current == goal:
            print(path)
            return
        
        if not graph[current]:
            print("No path found")
            return

        for n in graph[current]:
            open_list.append((n, g+1, path+[n]))
            
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
    "A":10,
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
    
a_star("A","H")    
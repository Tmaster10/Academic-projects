import heapq

# Define the graph with edges and costs (g-values)
graph = {
    'S': {'A': 5, 'B': 5, 'E': 7, "F": 3},
    'A': {"H": 6},
    'B': {"C": 6, "D": 3, "F": 6},
    'C': {'G1': 8},
    'D': {"C": 6},
    'E': {"B": 4, "D": 3, "J": 3, "K": 5},
    'F': {"A": 4, "E": 5},
    'H': {"F":2, "G1": 5, "I": 3},
    'I': {"F": 2, "G2": 4, "J": 6},
    'J': {"E": 2, "N": 5},
    'K': {"D": 3, "L": 7, "M": 5},
    'L': {"D": 4, "G1": 3, "G2": 5},
    'M': {"E":4, "G2": 2,"J": 3, "P":4},
    'N': {"G3": 6, "I": 4, "M":3},
    'P': {"G2":3, "N":2},
    'G1': {},
    'G2': {"G1":7, "K":6},
    'G3': {"N": 7}
}

# Heuristics for goal G2 (second column from the document)
heuristics = {
    'S': 3.00, 'A': 3.80, 'B': 2.10, 'C': 0.90, 'D': 1.30,
    'E': 2.10, 'F': 3.20, 'H': 3.80, 'I': 3.50, 'J': 2.80,
    'K': 1.60, 'L': 1.00, 'M': 2.20, 'N': 3.20, 'P': 2.70,
    'G1': 0, 'G2': 1.70, 'G3': 4.20
}

# A* Search Algorithm
def a_star_search(graph, start, goal, heuristics):
    open_list = []  # Priority queue (min-heap)
    heapq.heappush(open_list, (0 + heuristics[start], 0, start, []))  # (f, g, node, path)
    closed_set = set()  # To keep track of visited nodes
    
    while open_list:
        f, g, current_node, path = heapq.heappop(open_list)
        path = path + [current_node]
        
        if current_node == goal:
            return path, g  # Found the goal
        
        if current_node in closed_set:
            continue
        
        closed_set.add(current_node)
        
        for neighbor, cost in graph[current_node].items():
            if neighbor not in closed_set:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path))
    
    return None, float('inf')  # No path found

# Perform A* Search to find Goal 2 (G2)
path, total_cost = a_star_search(graph, 'S', 'G1', heuristics)
path, total_cost
print(path, total_cost) 
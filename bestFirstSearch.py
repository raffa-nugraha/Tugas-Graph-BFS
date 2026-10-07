import heapq

def best_first_search(graph, start, goal, heuristic):
    # Priority Queue (f(n), node)
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    
    visited = set()
    parent = {start: None}
    
    while open_list:
        # Mengambil node dengan f(n) terkecil
        f, current = heapq.heappop(open_list)
        
        if current in visited:
            continue
            
        visited.add(current)
        
        print(f"Visiting: {current}, f(n) = {f}")
        
        # Goal ditemukan
        if current == goal:
            return reconstruct_path(parent, goal)
            
        # Eksplorasi successor
        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                # Greedy Best-First Search: f(n) = h(n)
                heapq.heappush(
                    open_list,
                    (heuristic[neighbor], neighbor)
                )
                
    return None

def reconstruct_path(parent, goal):
    path = []
    current = goal
    
    while current is not None:
        path.append(current)
        current = parent[current]
        
    return path[::-1]

# Graph Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Heuristic h(n)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 3,
    'G': 0
}

# Inisialisasi Start dan Goal
start = 'A'
goal = 'G'

# Eksekusi pencarian
path = best_first_search(
    graph,
    start,
    goal,
    heuristic
)

print("\nPath:", path)
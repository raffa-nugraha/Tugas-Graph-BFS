import heapq

# --- Halaman 16 & 17: Fungsi Heuristic (Manhattan Distance) ---
def heuristic(node, goal):
    # h(n) = |x1 - x2| + |y1 - y2|
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

# --- Halaman 17 & 18: Fungsi Utama Best-First Search ---
def best_first_search(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    
    # Priority Queue: (f(n), node)
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), start))
    
    visited = set()
    parent = {start: None}
    
    # 4 Arah Pergerakan NPC: (dx, dy)
    directions = [
        (-1, 0), # Atas
        (1, 0),  # Bawah
        (0, -1), # Kiri
        (0, 1)   # Kanan
    ]
    
    while open_list:
        # Mengambil node dengan f(n) / h(n) terkecil
        f, current = heapq.heappop(open_list)
        
        # Jika sudah dikunjungi, skip
        if current in visited:
            continue
            
        visited.add(current)
        
        print(f"Visit {current}, h(n) = {f}")
        
        # Jika goal ditemukan
        if current == goal:
            return reconstruct_path(parent, goal)
            
        x, y = current
        
        # Mengecek semua kemungkinan gerakan (4 arah)
        for dx, dy in directions:
            next_x = x + dx
            next_y = y + dy
            next_node = (next_x, next_y)
            
            # 1. Cek apakah posisi berada di dalam batas map
            if not (0 <= next_x < rows and 0 <= next_y < cols):
                continue
                
            # 2. Cek apakah menabrak obstacle/dinding
            if grid[next_x][next_y] == '#':
                continue
                
            # 3. Cek apakah node sudah dikunjungi
            if next_node in visited:
                continue
                
            # Simpan parent
            if next_node not in parent:
                parent[next_node] = current
                
            # Greedy Best First Search: f(n) = h(n)
            h = heuristic(next_node, goal)
            heapq.heappush(open_list, (h, next_node))
            
    return None

# --- Halaman 18: Fungsi Rekonstruksi Jalur ---
def reconstruct_path(parent, goal):
    path = []
    current = goal
    
    while current is not None:
        path.append(current)
        current = parent[current]
        
    path.reverse() # Balik urutan: Start -> Goal
    return path

# --- Halaman 18: Fungsi Menampilkan Map dengan Jalur ---
def print_map(grid, path):
    # Copy grid agar tidak mengubah grid asli
    game_map = [row[:] for row in grid]
    
    # Tandai jalur dengan karakter '*'
    for x, y in path:
        if game_map[x][y] not in ['S', 'G']:
            game_map[x][y] = '*'
            
    print("\nGame Map:")
    for row in game_map:
        print(" ".join(row))

# --- Halaman 19: Inisialisasi Map, Start, Goal, dan Eksekusi ---
grid = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '#', '#', '.'],
    ['.', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (4, 4)

# Menjalankan Algoritma
path = best_first_search(grid, start, goal)

# --- Output Hasil ---
if path:
    print("\nPath ditemukan:")
    print(" -> ".join(str(node) for node in path))
    print("\nJumlah langkah:", len(path) - 1)
    print_map(grid, path)
else:
    print("\nPath tidak ditemukan.")
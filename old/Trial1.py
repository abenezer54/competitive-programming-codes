import tkinter as tk
from tkinter import messagebox
import queue
import time

# Initialize main window
root = tk.Tk()
root.title("Tree Search Algorithm Visualizer")
root.geometry("800x600")

# Variables
graph = {}
positions = {}

# Parse the graph input
def parse_graph(input_text):
    lines = input_text.strip().splitlines()
    graph.clear()
    for line in lines:
        parts = line.split(":")
        if len(parts) != 2:
            messagebox.showerror("Input Error", "Each line should be in format 'node:neighbor1,neighbor2,...'")
            return False
        node = parts[0].strip()
        neighbors = parts[1].strip().split(",") if parts[1].strip() else []
        graph[node] = [neighbor.strip() for neighbor in neighbors if neighbor.strip()]
    return True

# BFS with goal node search
def bfs_algorithm(start_node, goal_node):
    if start_node not in graph:
        messagebox.showerror("Error", "Start node not in graph")
        return
    
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    visited.add(start_node)
    
    canvas.delete("all")  # Clear the canvas before drawing
    draw_tree_layout()  # Draw initial nodes and edges
    
    while not q.empty():
        current_node = q.get()
        x, y = positions[current_node]
        
        # Highlight the current node
        canvas.itemconfig(nodes[current_node], fill="green")
        root.update()
        time.sleep(0.5)
        
        if current_node == goal_node:
            messagebox.showinfo("Search Result", f"Goal node '{goal_node}' found!")
            return
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                q.put(neighbor)
        
        # Mark as visited
        canvas.itemconfig(nodes[current_node], fill="lightblue")
    
    messagebox.showinfo("Search Result", f"Goal node '{goal_node}' not found.")

# DFS with goal node search
def dfs_algorithm(start_node, goal_node):
    if start_node not in graph:
        messagebox.showerror("Error", "Start node not in graph")
        return

    visited = set()
    stack = [start_node]
    visited.add(start_node)
    
    canvas.delete("all")
    draw_tree_layout()
    
    while stack:
        current_node = stack.pop()
        x, y = positions[current_node]
        
        # Highlight the current node
        canvas.itemconfig(nodes[current_node], fill="green")
        root.update()
        time.sleep(0.5)
        
        if current_node == goal_node:
            messagebox.showinfo("Search Result", f"Goal node '{goal_node}' found!")
            return
        
        for neighbor in reversed(graph.get(current_node, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
        
        # Mark as visited
        canvas.itemconfig(nodes[current_node], fill="lightblue")
    
    messagebox.showinfo("Search Result", f"Goal node '{goal_node}' not found.")

# Depth-Limited Search (DLS) with goal node search
def dls_algorithm(start_node, goal_node, limit):
    def dls_recursive(node, depth):
        if depth > limit:
            return False
        
        x, y = positions[node]
        canvas.itemconfig(nodes[node], fill="green")
        root.update()
        time.sleep(0.5)
        
        if node == goal_node:
            return True
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                if dls_recursive(neighbor, depth + 1):
                    return True
        
        canvas.itemconfig(nodes[node], fill="lightblue")  # Mark as visited
        return False
    
    if start_node not in graph:
        messagebox.showerror("Error", "Start node not in graph")
        return
    
    visited = set()
    visited.add(start_node)
    canvas.delete("all")
    draw_tree_layout()
    
    found = dls_recursive(start_node, 0)
    if found:
        messagebox.showinfo("Search Result", f"Goal node '{goal_node}' found!")
    else:
        messagebox.showinfo("Search Result", f"Goal node '{goal_node}' not found.")

# Function to select algorithm
def select_algorithm():
    algorithm = algorithm_var.get()
    start_node = start_node_entry.get().strip()
    goal_node = goal_node_entry.get().strip()
    
    if algorithm == "BFS":
        bfs_algorithm(start_node, goal_node)
    elif algorithm == "DFS":
        dfs_algorithm(start_node, goal_node)
    elif algorithm == "Depth-Limited Search":
        limit = int(limit_entry.get()) if limit_entry.get().isdigit() else 2
        dls_algorithm(start_node, goal_node, limit)
    else:
        messagebox.showinfo("Info", f"{algorithm} not yet implemented.")

# Function to set up a hierarchical tree layout
def draw_tree_layout():
    global nodes
    nodes = {}
    level_map = {}
    
    def build_levels(node, level=0):
        if node not in level_map:
            level_map[node] = level
        for child in graph.get(node, []):
            build_levels(child, level + 1)
    
    root_node = list(graph.keys())[0]
    build_levels(root_node)
    
    max_level = max(level_map.values())
    level_positions = {level: [] for level in range(max_level + 1)}
    for node, level in level_map.items():
        level_positions[level].append(node)
    
    for level in range(max_level + 1):
        nodes_in_level = level_positions[level]
        x_spacing = 800 // (len(nodes_in_level) + 1)
        y = 100 + level * 100
        for i, node in enumerate(nodes_in_level):
            x = (i + 1) * x_spacing
            positions[node] = (x, y)
            node_circle = canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightgrey")
            nodes[node] = node_circle
            canvas.create_text(x, y, text=node)
            for parent, children in graph.items():
                if node in children:
                    px, py = positions[parent]
                    canvas.create_line(px, py + 20, x, y - 20)
    
    # Update the scrollregion based on the canvas size
    canvas.config(scrollregion=canvas.bbox("all"))

# Set Graph Button Command
def set_graph():
    input_text = graph_input_text.get("1.0", tk.END)
    if parse_graph(input_text):
        messagebox.showinfo("Success", "Graph set successfully!")
        draw_tree_layout()

# GUI Layout
graph_input_label = tk.Label(root, text="Enter Tree Graph (e.g., A:B,C\nB:D,E\nC:F,G):")
graph_input_label.pack()
graph_input_text = tk.Text(root, height=5, width=40)
graph_input_text.pack()
set_graph_button = tk.Button(root, text="Set Graph", command=set_graph)
set_graph_button.pack(pady=5)

start_node_label = tk.Label(root, text="Enter Start Node:")
start_node_label.pack()
start_node_entry = tk.Entry(root)
start_node_entry.pack(pady=5)

goal_node_label = tk.Label(root, text="Enter Goal Node:")
goal_node_label.pack()
goal_node_entry = tk.Entry(root)
goal_node_entry.pack(pady=5)

algorithm_var = tk.StringVar(root)
algorithm_var.set("BFS")
algorithm_menu = tk.OptionMenu(root, algorithm_var, "BFS", "DFS", "Depth-Limited Search", 
                               "Uniform Cost Search", "Iterative Deepening DFS", 
                               "Bidirectional Search", "Informed Search", "Pure Heuristic", 
                               "Best-First Search", "A* Search")
algorithm_menu.pack(pady=5)

limit_label = tk.Label(root, text="Depth Limit (for DLS):")
limit_label.pack()
limit_entry = tk.Entry(root)
limit_entry.pack(pady=5)

start_button = tk.Button(root, text="Run Algorithm", command=select_algorithm)
start_button.pack(pady=10)

# Create a scrollable canvas
canvas_frame = tk.Frame(root)
canvas_frame.pack(fill="both", expand=True)

canvas_scrollbar_y = tk.Scrollbar(canvas_frame, orient="vertical")
canvas_scrollbar_y.pack(side="right", fill="y")

canvas_scrollbar_x = tk.Scrollbar(canvas_frame, orient="horizontal")
canvas_scrollbar_x.pack(side="bottom", fill="x")

canvas = tk.Canvas(canvas_frame, width=800, height=400, bg="white", 
                   yscrollcommand=canvas_scrollbar_y.set, xscrollcommand=canvas_scrollbar_x.set)
canvas.pack(fill="both", expand=True)

# Configure the scrollbars to the canvas
canvas_scrollbar_y.config(command=canvas.yview)
canvas_scrollbar_x.config(command=canvas.xview)

root.mainloop()

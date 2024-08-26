import tkinter as tk
from tkinter import Canvas
import matplotlib.pyplot as plt
import networkx as nx
import os

class DFSVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DFS Algorithm Visualizer")
        self.geometry("800x600")

        # Create a Canvas for Matplotlib plot
        self.canvas = Canvas(self, width=800, height=600)
        self.canvas.pack()

        # Add a button to start the DFS algorithm
        self.start_button = tk.Button(self, text="Start DFS", command=self.start_dfs)
        self.start_button.pack()

        # Create a graph
        self.G = nx.Graph()
        self.pos = None

        # Add nodes and edges (Example graph)
        self.create_graph()

    def create_graph(self):
        # Create a sample graph
        self.G.add_edge(0, 1)
        self.G.add_edge(1, 2)
        self.G.add_edge(2, 3)
        self.G.add_edge(3, 4)
        self.G.add_edge(4, 0)
        self.G.add_edge(1, 3)
        self.G.add_edge(2, 4)

        # Set node positions
        self.pos = nx.spring_layout(self.G)

        # Draw the initial graph
        self.draw_graph()

    def draw_graph(self, nodes_to_highlight=None):
        if nodes_to_highlight is None:
            nodes_to_highlight = []

        plt.figure(figsize=(8, 6))
        nx.draw(self.G, pos=self.pos, with_labels=True, node_size=500, node_color='lightblue', font_size=16, font_weight='bold')
        nx.draw_networkx_edges(self.G, pos=self.pos)
        nx.draw_networkx_nodes(self.G, pos=self.pos, nodelist=nodes_to_highlight, node_color='red')

        # Display the plot in Tkinter
        temp_path = os.path.join(os.getenv('TEMP'), 'graph.png')
        plt.savefig(temp_path)
        self.canvas_image = tk.PhotoImage(file=temp_path)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.canvas_image)
        self.canvas.update()

    def start_dfs(self):
        visited = set()
        start_node = list(self.G.nodes())[0]
        self.dfs(start_node, visited)

    def dfs(self, node, visited):
        visited.add(node)
        self.draw_graph(nodes_to_highlight=list(visited))
        self.update()
        self.after(1000)  # Pause for a second to visualize each step

        for neighbor in self.G.neighbors(node):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

if __name__ == "__main__":
    app = DFSVisualizer()
    app.mainloop()

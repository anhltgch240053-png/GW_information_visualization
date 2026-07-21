import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def task_1():
    print("Task 1: Create a graph like the one have been shown")
    Graph1 = nx.Graph()

    position1 = {

        "Oxford Circus": (0, 4),
        "Piccadilly Circus": (1, 2),
        "Charing Cross": (2, 0),
        "Leicester Square": (2, 2),
        "Covent Garden": (3, 3)

    }

    edges1 = [
        ("Oxford Circus", "Piccadilly Circus", 0.7, "chocolate", "Bakerloo"),
        ("Piccadilly Circus", "Charing Cross", 0.6, "chocolate", "Bakerloo"),
        ("Piccadilly Circus", "Leicester Square", 0.4, "blue", "Piccadilly"),
        ("Leicester Square","Charing Cross", 0.4, "black", "Northern"),
        ("Leicester Square", "Covent Garden", 0.3, "blue", "Piccadilly")
    ]

    for u, v, dist, color, line in edges1:
        Graph1.add_edge(u, v, weight=dist, color=color, line=line)
        
    plt.figure(figsize=(8, 8))
    
    # 3. Vẽ các thành phần của đồ thị
    nx.draw_networkx_nodes(Graph1, position1, node_color='lightgray', node_size=600)
    
    edge_colors = [data['color'] for _, _, data in Graph1.edges(data=True)]
    nx.draw_networkx_edges(Graph1, position1, edge_color=edge_colors, width=3)
    
    label_positions = {
    "Oxford Circus": (0.6, 4),
    "Piccadilly Circus": (0.6, 2.2),
    "Charing Cross": (2.0, 0.2),
    "Leicester Square": (2.6, 1.8),
    "Covent Garden": (3.6, 3.0)
    }
    nx.draw_networkx_labels(
    Graph1,
    label_positions,
    font_size=10,
    font_family="sans-serif",
    )
    
    # Hiển thị số khoảng cách thay vì chữ cái a,b,c
    edge_labels = {(u, v): f"{data['weight']} km" for u, v, data in Graph1.edges(data=True)}
    nx.draw_networkx_edge_labels(Graph1, position1, edge_labels=edge_labels, font_size=9)
    
    # 4. Vẽ bảng chú giải (Key) khớp với hình mẫu
    bakerloo_line = mlines.Line2D([], [], color='chocolate', linewidth=3, label='Bakerloo')
    piccadilly_line = mlines.Line2D([], [], color='blue', linewidth=3, label='Piccadilly')
    northern_line = mlines.Line2D([], [], color='black', linewidth=3, label='Northern')
    
    plt.legend(handles=[piccadilly_line, northern_line, bakerloo_line], title="Key", loc="lower right", framealpha=1, edgecolor="black")
    plt.xlim(-0.5, 4.2)
    plt.ylim(-0.5, 4.5)
    plt.title("Task 1: Initial Transport Map")
    plt.axis("off") # Ẩn khung tọa độ
    plt.tight_layout()
    plt.savefig("task1.png") # Lưu ảnh để nộp
    plt.show()

if __name__ == "__main__":
    task_1()
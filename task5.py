import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import random

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=str(node.val))
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def insert_into_tree(arr, i, n):
    if i < n:
        node = Node(arr[i])
        node.left = insert_into_tree(arr, 2*i + 1, n)
        node.right = insert_into_tree(arr, 2*i + 2, n)
        return node
    return None

def get_color(step, total_steps):
    base_intensity = 230
    intensity = base_intensity - int((base_intensity - 100) * (step / total_steps))
    return f"#{intensity:02x}{intensity:02x}FF"

def dfs(node, step=0, total_steps=0):
    if node:
        node.color = get_color(step, total_steps)
        step += 1
        step = dfs(node.left, step, total_steps)
        step = dfs(node.right, step, total_steps)
    return step

def bfs(root, total_steps=0):
    queue = [root]
    step = 0
    while queue:
        node = queue.pop(0)
        if node:
            node.color = get_color(step, total_steps)
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def build_tree_from_heap(arr):
    n = len(arr)
    return insert_into_tree(arr, 0, n)


list = [random.randint(1, 1000) for _ in range(5)]
heapq.heapify(list)
title_text_dfs = "Depth First Search"
root = build_tree_from_heap(list)
dfs(root, 0, len(list))
draw_tree(root, title_text_dfs)

list = [random.randint(1, 1000) for _ in range(5)]
heapq.heapify(list)
title_text_dfs = "Breadth First Search"
root = build_tree_from_heap(list)
bfs(root, len(list))
draw_tree(root, title_text_dfs)


# Відображення бінарної купи
# draw_tree(root)

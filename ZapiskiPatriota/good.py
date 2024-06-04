import networkx as nx
import matplotlib.pyplot as plt

# Создание пустого графа
G = nx.DiGraph()  # DiGraph для направленного графа, Graph для ненаправленного

# Добавление вершин (людей)
people = ['Alice', 'Bob', 'Charlie', 'David']
G.add_nodes_from(people)

# Добавление дуг (отношений) с весами (интенсивностью)
relationships = [
    ('Alice', 'Bob', 5),
    ('Alice', 'Charlie', 3),
    ('Bob', 'Charlie', 2),
    ('Charlie', 'David', 4),
    ('David', 'Alice', 1)
]

G.add_weighted_edges_from(relationships)

# Визуализация графа
def draw_graph(G):
    # Позиционирование вершин
    pos = nx.spring_layout(G)

    # Рисование вершин
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # Рисование ребер
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2)

    # Рисование меток вершин
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    # Рисование меток ребер (весов)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Показ графа
    plt.title("Граф отношений между людьми")
    plt.show()

# Визуализируем граф
draw_graph(G)

# Анализ графа
# Найти кратчайший путь между двумя людьми
shortest_path = nx.shortest_path(G, source='Alice', target='David', weight='weight')
print("Кратчайший путь от Alice до David:", shortest_path)

# Найти центральность по степени
degree_centrality = nx.degree_centrality(G)
print("Центральность по степени:", degree_centrality)

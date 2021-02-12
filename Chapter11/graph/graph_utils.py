import random

from igraph import Graph, plot


def plot_graph(edges, vertex_color):
    g = Graph(directed = False)
    g.add_vertices(len(get_vertices_from_edges(edges)))

    for i in range(len(g.vs)):
        g.vs[i]["id"] = i
        g.vs[i]["label"] = str(i)
        g.vs[i]['color'] = vertex_color[i]

    g.add_edges(edges)

    visual_style = {
        "bbox":              (800, 800),
        "margin":            27,
        "vertex_size":       35,
        "vertex_label_size": 22,
        "edge_curved":       False,
        "layout":            g.layout_lgl()
    }
    plot(g, **visual_style)


def plot_graph_blank(edges):
    vertex_color = {}
    for v in get_vertices_from_edges(edges):
        vertex_color[v] = "white"

    plot_graph(edges, vertex_color)


def adjacent_vertices_same_color_count(edges, vertex_color):
    color_map = {}
    for vertex, color in vertex_color.items():
        if color not in color_map:
            color_map[color] = set()
        color_map[color].add(vertex)

    count = 0
    for edge in edges:
        for _, vertices in color_map.items():
            if set(edge) <= set(vertices):
                count += 1

    return count


def get_edges():
    return [
        (0, 2), (3, 4), (3, 5), (0, 5), (1, 4), (2, 10), (14, 8), (15, 3), (16, 9), (17, 11), (18, 7),
        (19, 7), (6, 3), (7, 6), (8, 0), (11, 5), (11, 9), (12, 1), (13, 4), (20, 5), (21, 17), (22, 15),
        (23, 20), (24, 20), (25, 17), (26, 24), (27, 10), (28, 15), (29, 21), (12, 14), (16, 20), (29, 19),
        (27, 22), (26, 9), (25, 26), (23, 10), (6, 28), (14, 13), (0, 12), (3, 2), (19, 14), (22, 10), (1, 18),
        (7, 21), (15, 12), (11, 1), (23, 28), (6, 11), (9, 25), (17, 9), (24, 16), (27, 28), (18, 20), (19, 21),
        (1, 14), (22, 29), (17, 4), (8, 13), (7, 23), (16, 28), (5, 9), (12, 29), (27, 21), (1, 23)
    ]


def get_vertices_from_edges(edges):
    all_vertices = set()
    for t in edges:
        all_vertices.add(t[0])
        all_vertices.add(t[1])
    return all_vertices


if __name__ == '__main__':
    random.seed(16)
    plot_graph_blank(get_edges())

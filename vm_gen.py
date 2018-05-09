from graphviz import Digraph


def create_graph(total, steps, initial=0):
    nodes, edges = create_graph_components(initial, steps, total)

    g = Digraph()

    for node in nodes:
        g.node(str(node))

    for edge in edges:
        g.edge(str(edge[0]), str(edge[1]), str(edge[1] - edge[0]))

    return g, nodes, edges


def create_graph_components(initial, increments, total):
    nodes = {initial}
    edges = set()

    while True:
        changed = False

        for node in tuple(nodes):  # Shallow copy of set
            for increment in increments:
                new_nodes, new_edges = progress_step(node, total, increment)

                edge_count = len(edges)

                nodes.update(new_nodes)
                edges.update(new_edges)

                changed = changed or edge_count != len(edges)

        if not changed:
            break

    return nodes, edges


def progress_step(start, stop, step):
    nodes = set()
    edges = set()
    node = start
    old_node = None

    while node <= stop:
        if old_node is not None:
            edges.add((old_node, node))

        nodes.add(node)

        old_node = node
        node += step

    return nodes, edges
